function getImageByAJAX() {
  var xhr = new XMLHttpRequest(); // Create an XMLHttpRequest object
  xhr.open("GET", "/get_example_img/", true); // Open a GET request to the image route

  xhr.onload = function () {
    if (xhr.status === 200) { // Check for successful response (200 OK)
      const imageUrl = xhr.responseText; // Get the image URL from the response
      const image = document.getElementById('example-faces-contactsheet'); // Assuming you have a container with id 'image-container'
      image.setAttribute('src', imageUrl);
      // image.style.width = 'parent';

    } else {
      console.error("Error fetching image:", xhr.statusText); // Handle errors
    }
  };

  xhr.send(); // Send the request


}

function getTextByAJAX() {
  var xhr = new XMLHttpRequest(); // Create an XMLHttpRequest object
  xhr.open("GET", "/get_example_text/", true); // Open a GET request to the image route

  xhr.onload = function () {
    if (xhr.status === 200) { // Check for successful response (200 OK)
      const text = xhr.responseText; // Get the image URL from the response
      const paragraphElement = document.getElementById("example-text");
      // const textContainer = document.getElementById('example-output-box'); // Assuming you have a container with id 'image-container'
      // const paragraphElement = textContainer.querySelector('p');
      paragraphElement.innerText = text;

    } else {
      console.error("Error fetching image:", xhr.statusText); // Handle errors
    }
  };

  xhr.send(); // Send the request


}

function toggleImage() {
  getImageByAJAX();
  getTextByAJAX();
}

//open upload handling
function uploadFile(){

  const formData = new FormData();
  const fileInput = document.getElementById('file');
  const file = fileInput.files[0];

    let myResponse;
    if (file) {
        formData.append('file', file);
        formData.append('name', name);

        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/upload/', true);

        xhr.onload = function () {
            const response = document.getElementById('upload-response');
            if (xhr.status === 200) {
                // response.innerHTML = '<p>' + JSON.parse(xhr.responseText).message + '</p>';
                myResponse = '<p>' + JSON.parse(xhr.responseText).message + '</p>';
            } else {
                // response.innerHTML = '<p>Error: ' + JSON.parse(xhr.responseText).error + '</p>';
                myResponse = '<p>Error: ' + JSON.parse(xhr.responseText).error + '</p>';
            }
            window.alert(myResponse)
        };

        xhr.send(formData);
    } else {
        const response = document.getElementById('upload-response');
        // response.innerHTML = '<p>Please select a file to upload.</p>';
        myResponse = '<p>Please select a file to upload.</p>';
        window.alert(myResponse)
    }

}
//close upload handling

//open user session handling
function user_login() {
    const formData = new FormData();
    const nameInput = document.getElementById('username');
    formData.append('username', nameInput.value);  // Use 'value' instead of 'innerText'

    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/login/', true);
    xhr.onload = function () {
        let current_user = "";
        let is_returning_user = "";
        if (xhr.status === 200) {
            current_user = JSON.parse(xhr.responseText).message;
            is_returning_user = JSON.parse(xhr.responseText).is_returning_user;  // Use 'JSON.parse' to parse the response text
            show_login_status(current_user) // show login status, display username is in session
            toggleUsername() //disable reentering another username while in session of the present one
            nameInput.value = ''; // clear input clear after successful login
            if (is_returning_user === true){
                window.alert("hello again " + current_user);
            } else {
                window.alert("hello new member " + current_user);
            }
            document.getElementById("current-user").innerText = current_user;

        } else {
            // response = JSON.parse(xhr.responseText).error;  // Use 'JSON.parse' to parse the response text
            console.error("Error fetching username:", xhr.statusText);
        }

    };
    xhr.send(formData);
}

function toggleUsername(){
    let field = document.getElementById("username");
    field.disabled = field.disabled !== true;
}

function user_logout(){
    toggleUsername();
    document.getElementById('login-status').innerHTML = 'Hello Anonymous Visitor';
    document.getElementById('current-user').innerText = '';

    let xhr = new XMLHttpRequest();
    xhr.open('GET', '/logout/', true);
    xhr.onload = function () {
        if (xhr.status === 200) {
            window.alert('You have successfully logged out.');
        }
        else {
            window.alert('Logging out failed, please try again')
        }
    }
    xhr.send();
    //we will add the AJAX code later
    //also we are going to take care of the session stuff
}

function show_login_status(username){
    let status = document.getElementById('login-status');
    status.innerText = 'Hello ' + username;
}

function get_session_data(callback){
    const xhr = new XMLHttpRequest();
    xhr.open('GET', '/get_session/', true);
    xhr.onload = function () {
        if (xhr.status === 200) {
            let response = JSON.parse(xhr.responseText);
            console.log("this is the type of response from AJAX : " + typeof response);
            callback(response);
            }
        }
    xhr.send();
}
function get_session_data(){
    const xhr = new XMLHttpRequest();
    xhr.open('GET', '/get_session/', true);
    xhr.onload = function () {
        if (xhr.status === 200) {
            let response = JSON.parse(xhr.responseText);
            console.log("this is the type of response from AJAX : ");
            console.log(Object.entries(response));

            }
        }
    xhr.send();
}


//close user session handling

//open get user list
function get_users() {
  const xhr = new XMLHttpRequest();
  xhr.open('GET', '/get_users/', true);
  xhr.onload = function () {
    if (xhr.status === 200) {
      let users = JSON.parse(xhr.responseText);
      let user_list = document.getElementById('existing-users');
      console.log(users);
      console.log(typeof users); // This should be "object" now

      for (const user of users) { // Loop through the user objects in the array
        const listItem = document.createElement('li');
        listItem.textContent = user; // Assuming "name" is a property in the user object
        user_list.appendChild(listItem);
      }
    }
  };
  xhr.send();
}

function get_available_files_for_current_user(){
    const xhr = new XMLHttpRequest();
    xhr.open('GET', '/get_available_files/', true);
    xhr.onload = function () {
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);
            if ('message' in response) {
                window.alert(response.message);
            }
            else{
                let file_list = document.getElementById('user-file-list')
                file_list.replaceChildren()
                for (const file of Object.keys(response)){
                   const fileSwitch = document.createElement('div');
                   fileSwitch.setAttribute('class', 'form-check form-switch');

                    // Create the input element with the necessary attributes
                    const inputElement = document.createElement('input');
                    inputElement.setAttribute('class', 'form-check-input');
                    inputElement.setAttribute('type', 'checkbox');
                    inputElement.setAttribute('role', 'switch');
                    inputElement.setAttribute('id', 'flexSwitchCheckDefault');

                    // Create the label element with the necessary attributes
                    const labelElement = document.createElement('label');
                    labelElement.setAttribute('class', 'form-check-label');
                    labelElement.setAttribute('for', 'flexSwitchCheckDefault');
                    labelElement.textContent = file;

                    // Append the input and label elements to the div
                    fileSwitch.appendChild(inputElement);
                    fileSwitch.appendChild(labelElement);

                   file_list.append(fileSwitch)

                    //attach event listeners for unique selection
                    document.querySelectorAll('.form-check-input').forEach(switchElement => {
                            switchElement.addEventListener('change', function (event) {
                                const switches = document.querySelectorAll('.form-check-input');

                                switches.forEach(switchElement => {
                                    if (switchElement !== event.target) {
                                        switchElement.checked = false;
                                    }
                                });
                            });
                    });
                }
            }
        }
    }
    xhr.send();
}

//close get user list

//open get user file selection
function get_checked_file_switch() {
    const switchList = document.querySelectorAll('.form-check-input');
    let selectedSwitch;
    let filename;

    for (const switchElement of switchList) {
        if (switchElement.checked) {
            selectedSwitch = switchElement;
            break;  // Assuming only one switch can be checked at a time, exit the loop early.
        }
    }

    if (selectedSwitch) {
        filename = selectedSwitch.nextElementSibling.textContent;
        console.log(filename);  // Get the label's text content
    } else {
        console.log('No switch is checked.');
    }
    return filename;
}

function extract_selected_file(){
    const filename = get_checked_file_switch();

    //make ajax request to extract file
    const xhr = new XMLHttpRequest();
    xhr.open('GET', `/extract_selected_file/?filename=${encodeURIComponent(filename)}`, true);
    xhr.onload = function () {
       //operations
       if (xhr.status === 200) {
           let response = JSON.parse(xhr.responseText);
       }
    }
    xhr.send();
}

//close get user file selection

