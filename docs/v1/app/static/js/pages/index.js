
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

	inputElement.value = greetingsText;
}
document.addEventListener('DOMContentLoaded', updateGreetings);