const toggleActiveCol = () => {
    const allColumnToClick  = document.querySelectorAll(".head-tab-click");
    const allDataColumn     = document.querySelectorAll(".col-content-contants");
    const addTextButtons    = document.querySelectorAll(".add_contact"); 

    allColumnToClick.forEach(btn => {
        btn.addEventListener("click", function () {
            const activeColumnToClick = document.querySelector(".head-tab-click.active");
            const activeDataColumn = document.querySelector(".col-content-contants.active"); 

            if (btn !== activeColumnToClick) {
                activeColumnToClick.classList.remove("active");
                btn.classList.add("active");

                const currentActiveIndex = parseInt(btn.classList[1].split("-")[1]);

                if (activeDataColumn) {
                    activeDataColumn.classList.remove("active");
                }

                allDataColumn[currentActiveIndex].classList.add("active");

                const activeAddTextButton = document.querySelector(".add_contact.active"); 
                if (activeAddTextButton) {
                    activeAddTextButton.classList.remove("active");
                }

                addTextButtons[currentActiveIndex].classList.add("active");
            }
        });
    });
};


/* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */
/*       mobile | card more functions      */
/* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */

const cardmoreFunctionsOnMobile = () => {
    const cards = document.querySelectorAll(".cards_container");

    cards.forEach(card => {
        var more_dunc = card.querySelector(".more_info")
        more_dunc.addEventListener("click", function () {
            more_dunc.classList.toggle("active");    
        })
    })

}



document.addEventListener('DOMContentLoaded', function () {
    toggleActiveCol();
    cardmoreFunctionsOnMobile();
});