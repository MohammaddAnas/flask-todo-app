document.addEventListener("DOMContentLoaded", function () {

  const navbar = document.querySelector(".navbar");
  const form = document.querySelector("form");

  /* ===== GLOBAL CLICK HANDLER ===== */
  document.body.addEventListener("click", function (e) {

    const todo = e.target.closest(".list-group-item");
    if (!todo) return;

    // BUTTON POP EFFECT
    if (e.target.tagName === "BUTTON") {
      e.target.classList.add("btn-pop");
      setTimeout(() => e.target.classList.remove("btn-pop"), 200);

      // DELETE
      todo.style.opacity = "0";
      todo.style.transform = "scale(0.9)";
      todo.style.transition = "all 0.3s ease";

      animateNavbar();
      showPopup("Todo deleted 🗑");

      setTimeout(() => todo.remove(), 300);
      return;
    }

    // UPDATE / COMPLETE
    todo.classList.toggle("completed");
    animateNavbar();

    showPopup(
      todo.classList.contains("completed")
        ? "Todo completed ✔"
        : "Todo updated ✏️"
    );
  });

  /* ===== FORM SUBMIT ===== */
  if (form) {
    form.addEventListener("submit", function () {
      animateNavbar();
      showPopup("Todo added 🎉");
    });
  }

  /* ===== NAVBAR ANIMATION ===== */
  function animateNavbar() {
    if (!navbar) return;
    navbar.classList.add("navbar-animate");
    setTimeout(() => navbar.classList.remove("navbar-animate"), 400);
  }

});

/* ===== POPUP FUNCTION ===== */
function showPopup(message) {
  const popup = document.createElement("div");
  popup.className = "popup";
  popup.innerText = message;

  document.body.appendChild(popup);

  setTimeout(() => {
    popup.style.opacity = "0";
    setTimeout(() => popup.remove(), 300);
  }, 2000);
}
