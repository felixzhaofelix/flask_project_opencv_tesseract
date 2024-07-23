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

function get_session_data(){
    const xhr = new XMLHttpRequest();
    xhr.open('GET', '/get_session/', true);
    xhr.onload = function () {
        if (xhr.status === 200) {
            let response = JSON.parse(xhr.responseText);
            console.log(response);
            }
        }
    xhr.send();
}



//close user session handling