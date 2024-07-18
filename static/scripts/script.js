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
  // var imageContainer = document.getElementById("image-container");
  // var image = imageContainer.querySelector("img"); // Check for existing image element



  // if (!image) { // If no image element exists
  //   getImageByAJAX(); // Fetch the image URL
  // } else {
  //   image.style.display = image.style.display === 'none' ? 'block' : 'none'; // Toggle display based on current state
  // }
}
