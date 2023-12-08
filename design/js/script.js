var dateEl = document.getElementById("date");
var timeEl = document.getElementById("time");

document.getElementById("date-output").innerHTML = dateEl.type === "date";
document.getElementById("time-output").innerHTML = timeEl.type === "time";

tinymce.init({
  selector: "#mytextarea",
});
