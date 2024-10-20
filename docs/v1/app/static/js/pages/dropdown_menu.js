document.addEventListener("DOMContentLoaded", function () {
    const dropdownContent = document.querySelector(".dropdown_menu_content");
    const dropdownList = document.querySelector(".dropdown_list");
    const dropdownIcon = document.querySelector(".dropdown_menu_content i");
    const dropdownTitleIcon = document.querySelector(".dropdown_title i");
  
    dropdownContent.addEventListener("click", function () {
        const isOpen = dropdownList.style.display === "block";
        dropdownList.style.display = isOpen ? "none" : "block";
        dropdownIcon.classList.toggle("rotate", !isOpen);
        dropdownTitleIcon.classList.toggle("rotate", !isOpen);
    });
  
    dropdownList.querySelectorAll("li:not(.dropdown_title)").forEach((item) => {
        item.addEventListener("click", function (event) {
            event.stopPropagation();
            item.classList.toggle("active");
            updateSelectedTags();
        });
    });
  
    document.addEventListener("click", function (event) {
        if (!dropdownContent.contains(event.target)) {
            dropdownList.style.display = "none";
            dropdownIcon.classList.remove("rotate");
            dropdownTitleIcon.classList.remove("rotate");
        }
    });
  
    function updateSelectedTags() {
        const selectedItems = Array.from(dropdownList.querySelectorAll("li.active"))
            .map((item) => item.textContent)
            .join(", ");
        
        dropdownContent.childNodes[0].nodeValue = selectedItems || "Choose tags";
    }
  }); 