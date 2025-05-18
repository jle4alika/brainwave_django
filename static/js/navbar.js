 document.addEventListener("DOMContentLoaded", () => {
    const burger = document.getElementById("burgerBtn");
    const sidebar = document.getElementById("mobileSidebar");
    const closeBtn = document.getElementById("sidebarCloseBtn");

    burger.addEventListener("click", () => {
      sidebar.classList.add("active");
      document.body.style.overflow = "hidden";
    });

    closeBtn.addEventListener("click", () => {
      sidebar.classList.remove("active");
      document.body.style.overflow = "";
    });

    sidebar.addEventListener("click", e => {
      if (e.target === sidebar) {
        sidebar.classList.remove("active");
        document.body.style.overflow = "";
      }
    });
  });
