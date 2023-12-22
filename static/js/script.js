// Verify if id exist element
function verify_exist(id) {
  // takes only id
  var element = document.getElementById(id);

  if (typeof element != "undefined" && element != null) {
    return true;
  } else {
    return false;
  }
}

// Tiny Initialization
tinymce.init({
  menubar: false,
  selector: "#event_description",
  plugins:
    "autolink charmap codesample emoticons link lists table visualblocks wordcount",
  toolbar:
    "blocks fontfamily fontsize | bold italic underline | link image media table | align lineheight  |  numlist bullist | emoticons charmap | removeformat",
  toolbar_mode: "sliding",
  elementpath: false,
  tinycomments_mode: "embedded",
  placeholder: "Whats your event about!",
  branding: false,
});

// Current Date and Time insertion
if (verify_exist("date")) {
  // Dom management for Date time picker
  document.addEventListener("DOMContentLoaded", function () {
    var today = new Date().toISOString().split("T")[0];
    var dateInput = document.getElementById("date");
    dateInput.setAttribute("min", today);
    dateInput.value = today;
  });

  document.addEventListener("DOMContentLoaded", function () {
    var today = new Date().toISOString().split("T")[0];
    document.getElementById("date").setAttribute("min", today);
  });
}

if (verify_exist("time")) {
  document.addEventListener("DOMContentLoaded", function () {
    var currentTime = new Date().toLocaleTimeString("en-GB", {
      hour: "2-digit",
      minute: "2-digit",
      hour12: false,
    });
    document.getElementById("time").value = currentTime;
  });
}

// Display image when uploading
$(function () {
  $(":file").change(function () {
    if (this.files && this.files[0]) {
      var reader = new FileReader();
      reader.onload = imageIsLoaded;
      reader.readAsDataURL(this.files[0]);
    }
  });
});

function imageIsLoaded(e) {
  $("#uploaded-image").attr("src", e.target.result);
}

// Verify if emails or passwords matches
if (verify_exist("signup")) {
  document
    .getElementById("signup")
    .addEventListener("submit", function (event) {
      var email = document.getElementById("email").value;
      var confirmedEmail = document.getElementById("confirmed_email").value;

      var password = document.getElementById("password").value;
      var confirmedPassword =
        document.getElementById("confirmed_password").value;

      if (email !== confirmedEmail) {
        event.preventDefault(); // Prevent form submission
        document.getElementById("error-message-email").textContent =
          "Emails do not match!";
      } else {
        document.getElementById("error-message-email").textContent = "";
      }

      if (password !== confirmedPassword) {
        event.preventDefault(); // Prevent form submission
        document.getElementById("error-message-password").textContent =
          "Password do not match!";
      } else {
        document.getElementById("error-message-password").textContent = "";
      }
    });
}
