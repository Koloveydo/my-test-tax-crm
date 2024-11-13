const toggleActiveCol = () => {
    const allColumnToClick  = document.querySelectorAll(".head-tab-click"); // Вкладки
    const allDataColumn     = document.querySelectorAll(".col-content-contants"); // Колонки з даними
    const addTextButtons    = document.querySelectorAll(".add_contact"); // Кнопки для зміни тексту

    allColumnToClick.forEach(btn => {
        btn.addEventListener("click", function () {
            const activeColumnToClick = document.querySelector(".head-tab-click.active"); // Поточна активна вкладка
            const activeDataColumn = document.querySelector(".col-content-contants.active"); // Поточна активна колонка

            if (btn !== activeColumnToClick) {
                // Скидаємо клас "active" з поточної вкладки
                activeColumnToClick.classList.remove("active");
                btn.classList.add("active");

                // Визначаємо індекс вкладки
                const currentActiveIndex = parseInt(btn.classList[1].split("-")[1]);

                // Скидаємо клас "active" з поточної колонки
                if (activeDataColumn) {
                    activeDataColumn.classList.remove("active");
                }

                // Додаємо клас "active" до нової колонки
                allDataColumn[currentActiveIndex].classList.add("active");

                // Скидаємо клас "active" з поточної кнопки
                const activeAddTextButton = document.querySelector(".add_contact.active"); // Поточна активна кнопка
                if (activeAddTextButton) {
                    activeAddTextButton.classList.remove("active");
                }

                // Додаємо клас "active" до відповідної кнопки
                addTextButtons[currentActiveIndex].classList.add("active");
            }
        });
    });
};

document.addEventListener('DOMContentLoaded', function () {
    toggleActiveCol();
});