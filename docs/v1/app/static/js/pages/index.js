
function updateGreetings(){
	const inputElement = document.getElementById("greetings_value")
	const now = new Date();
	const hours = now.getHours();
	let greetingsText;

	if (hours >= 5 && hours < 12) {
		greetingsText = "Good morning,";
	} else if (hours >= 12 && hours < 18){
		greetingsText = "Good afternoon,";
	} else if (hours >= 18 && hours < 22){
		greetingsText = "Good evening,";
	} else {
		greetingsText = "Good night,";
	}

	inputElement.textContent = greetingsText;
}
document.addEventListener('DOMContentLoaded', updateGreetings);

document.addEventListener("DOMContentLoaded", function () {
    const visitedButton = document.getElementById("visited_arrow_container");
	const visitedArrov = document.getElementById("visited_arrow");
    const workspaceDisplay = document.getElementById("workspace");
	const unmessButton = document.getElementById("unmess_arrow_container");
	const unmessArrow = document.getElementById("unmess_arrow");
	const inboxDisplay = document.getElementById("inbox");

    visitedButton.addEventListener("click", function () {
        workspaceDisplay.classList.toggle("active");
        visitedArrov.classList.toggle("active");
    });

	unmessButton.addEventListener("click", function () {
        inboxDisplay.classList.toggle("active");
        unmessArrow.classList.toggle("active");
    });
});

const navWorkspace = document.querySelectorAll('.workspace_table_btn');
navWorkspace.forEach(item => {
    item.addEventListener('click', () => {
        const href = item.getAttribute('data-href');
        if (href) {
            window.location.href = href;
        }
    });
});

document.querySelector(".no_invite_btn").addEventListener("click", function(){
	const inviteTable = document.querySelector(".unmess_invite");
	const inviteLine = document.querySelector(".line");
	inviteTable.style.display = 'none';
	inviteLine.style.display = 'none';
});