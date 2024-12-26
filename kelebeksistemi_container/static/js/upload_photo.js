// JavaScript to handle the upload button click
document.querySelector('.upload-btn').addEventListener('click', function() {
    // Trigger the hidden file input
    document.getElementById('fileInput').click();
  });
  
  // JavaScript to handle the selected file when the user chooses a new photo
  document.getElementById('fileInput').addEventListener('change', function(event) {
    // Here, you can handle the uploaded file (e.g., display the new photo or upload it to a server)
    const file = event.target.files[0];
    // Your upload logic here...
  });
  