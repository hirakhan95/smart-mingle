// Tiny Initialization
tinymce.init({
  menubar: false,
  selector: "textarea",
  plugins:
    "autolink charmap codesample emoticons link lists table visualblocks wordcount checklist casechange export permanentpen footnotes advtemplate advtable advcode editimage tableofcontents mergetags powerpaste tinymcespellchecker autocorrect a11ychecker typography inlinecss",
  toolbar:
    "blocks fontfamily fontsize | bold italic underline | link image media table mergetags | align lineheight | tinycomments | checklist numlist bullist | emoticons charmap | removeformat",
  toolbar_mode: "sliding",
  elementpath: false,
  tinycomments_mode: "embedded",
  placeholder: "Whats your event about!",
  branding: false,
});

// Dom management for Date time picker
document.addEventListener("DOMContentLoaded", function () {
  var today = new Date().toISOString().split("T")[0];
  var dateInput = document.getElementById("date");
  dateInput.setAttribute("min", today);
  dateInput.value = today;
});

document.addEventListener("DOMContentLoaded", function () {
  var currentTime = new Date().toLocaleTimeString("en-GB", {
    hour: "2-digit",
    minute: "2-digit",
    hour12: false,
  });
  document.getElementById("time").value = currentTime;
});

document.addEventListener("DOMContentLoaded", function () {
  var today = new Date().toISOString().split("T")[0];
  document.getElementById("date").setAttribute("min", today);
});

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
