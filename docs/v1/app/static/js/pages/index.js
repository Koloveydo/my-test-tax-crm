var now = new Date();
var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
var datetime = now.toLocaleDateString('en-US', options);

document.getElementById("datetime").value = datetime;


function updateGreetings(){
	const inputElement = document.getElementById("greetings_value")
	const now = new Date();
	const hours = now.getHours();
	let greetingsText;

	if (hours >= 5 && hours < 12) {
		greetingsText = "Good morning, have a nice day!";
	} else if (hours >= 12 && hours < 18){
		greetingsText = "Good afternoon, you're doing great work!";
	} else if (hours >= 18 && hours < 22){
		greetingsText = "Good evening, you're very diligent!";
	} else {
		greetingsText = "Good night, my master!";
	}

	inputElement.value = greetingsText;
}
document.addEventListener('DOMContentLoaded', updateGreetings);