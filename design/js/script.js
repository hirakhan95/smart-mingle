//
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

document.addEventListener("DOMContentLoaded", function () {
  var today = new Date().toISOString().split("T")[0];
  var dateInput = document.getElementById("date");
  dateInput.setAttribute("min", today);
  dateInput.value = today;
});
