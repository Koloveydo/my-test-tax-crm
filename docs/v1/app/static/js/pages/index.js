var now = new Date();
var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
var datetime = now.toLocaleDateString('en-US', options);

document.getElementById("datetime").value = datetime;


function updateGreetings(){
	const inputElement = document.getElementById("greetings_value")
	const inputElements = document.getElementById("greetings_values")
	const now = new Date();
	const hours = now.getHours();
	let greetingsText;
	let greetingsTexts;

	if (hours >= 5 && hours < 12) {
		greetingsText = "Good morning,";
		greetingsTexts = "have a nice day!";
		document.getElementById("greetings_values").style.display = "block";
	} else if (hours >= 12 && hours < 18){
		greetingsText = "Good afternoon,";
		greetingsTexts = "you're doing great work!";
		document.getElementById("greetings_values").style.display = "block";
	} else if (hours >= 18 && hours < 22){
		greetingsText = "Good evening,";
		greetingsTexts = "you're very diligent!";
		document.getElementById("greetings_values").style.display = "block";
	} else {
		greetingsText = "Good night, my master!";
	}

	inputElement.value = greetingsText;
	inputElements.value = greetingsTexts;
}
document.addEventListener('DOMContentLoaded', updateGreetings);