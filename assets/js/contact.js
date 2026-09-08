(function () {
  "use strict";

  var contactButton = document.querySelector(".contact-email");
  var contactStatus = document.getElementById("contact-email-status");

  if (!contactButton || !contactStatus) return;

  function emailAddress() {
    return ["michal", "tyrolski"].join(".") + String.fromCharCode(64) + ["gmail", "com"].join(".");
  }

  function setStatus(message) {
    contactStatus.textContent = message;
  }

  contactButton.addEventListener("click", function () {
    var address = emailAddress();

    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(address).then(function () {
        setStatus("Email address copied.");
      }, function () {
        window.location.href = "mailto:" + address;
        setStatus("Your email application is opening.");
      });
      return;
    }

    window.location.href = "mailto:" + address;
    setStatus("Your email application is opening.");
  });
}());
