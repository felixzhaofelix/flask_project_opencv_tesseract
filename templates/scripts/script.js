
// const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
// const popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
//   return new bootstrap.Popover(popoverTriggerEl);
// });
//
// const triggerTabList = document.querySelectorAll('#myTab button')
// triggerTabList.forEach(triggerEl => {
//   const tabTrigger = new bootstrap.Tab(triggerEl)
//
//   triggerEl.addEventListener('click', event => {
//     event.preventDefault()
//     tabTrigger.show()
//   })
// })

function getImage() {
  var xhr = new XMLHttpRequest(); // Create an XMLHttpRequest object
  xhr.open("GET", "/get_image/", true); // Open a GET request to the image route


  xhr.onload = function() {
    if (xhr.status === 200) { // Check for successful response (200 OK)
      var imageContainer = document.getElementById("image-container");
      var imageUrl = xhr.responseText; // Get the image URL from the response
      imageContainer.innerHTML = "<img id='big-img' src='" + imageUrl + "' alt='Image' width='30%'>";
    } else {
      console.error("Error fetching image:", xhr.statusText); // Handle errors
    }
  };

  xhr.send(); // Send the request
}
function toggleImage() {
  var imageContainer = document.getElementById("image-container");
  var image = imageContainer.querySelector("img"); // Check for existing image element

  if (!image) { // If no image element exists
    getImage(); // Fetch the image URL
  } else {
    image.style.display = image.style.display === 'none' ? 'block' : 'none'; // Toggle display based on current state
  }
}
