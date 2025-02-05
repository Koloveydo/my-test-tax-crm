document.addEventListener("DOMContentLoaded", function () {
    const tableContainer = document.querySelector(".table-container");

    tableContainer.addEventListener("wheel", function (event) {
        if (event.shiftKey) {
            event.preventDefault();
            tableContainer.scrollLeft += event.deltaY;
        }
    });
});
