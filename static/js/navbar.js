window.onload = function () {
	const bars = document.getElementById("bars");
  const ul = document.getElementById("navbar-ul");

  bars.addEventListener("click", () => {
    ul.classList.toggle("show");
    console.log("Event Handler: Clicked on hamburger");
  });
};
