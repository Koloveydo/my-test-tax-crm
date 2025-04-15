document.addEventListener("DOMContentLoaded", function(){
    const sentBtn = document.getElementById("sent_btn");
    const sheduledBtn = document.getElementById("sheduled_btn");
    const sentLine = document.getElementById("sent_line");
    const sheduledLine = document.getElementById("sheduled_line");
    const sentTable = document.getElementById("sent_table");
    const sheduledTable = document.getElementById("sheduled_table");
    sentBtn.addEventListener("click", function(){
        sentLine.classList.add("active");
        sheduledLine.classList.remove("active");
        sentTable.classList.add("active");
        sheduledTable.classList.remove("active");
    });
    sheduledBtn.addEventListener("click", function(){
        sentLine.classList.remove("active");
        sheduledLine.classList.add("active");
        sentTable.classList.remove("active");
        sheduledTable.classList.add("active");
    });
})