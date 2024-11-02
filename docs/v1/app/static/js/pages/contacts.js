const toggleActiveCol = () => {
    const allColumnToClick  = document.querySelectorAll(".head-tab-click");
    const allDataColumn     = document.querySelectorAll(".col-content-contants");

    allColumnToClick.forEach(btn => {
        btn.addEventListener("click", function () {
            var activeColumnToClick = document.querySelector(".head-tab-click.active");

            if (btn !== activeColumnToClick) {
                activeColumnToClick.classList.toggle("active");
                btn.classList.toggle("active");

                var currentActiveIndex = parseInt(btn.classList[1].split("-")[1]);

                document.querySelector(".col-content-contants.active").classList.toggle("active");
                allDataColumn[currentActiveIndex].classList.toggle("active");
            }
        })
    })

}

document.addEventListener('DOMContentLoaded', function () {
    toggleActiveCol();


})