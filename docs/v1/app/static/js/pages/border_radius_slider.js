const radiusSlider = document.querySelector('.radiusSlider');
const sliderValue = document.querySelector('.sliderValue');

function FillSlider() {
    const value = (radiusSlider.value - radiusSlider.min) / (radiusSlider.max - radiusSlider.min) * 100;
    radiusSlider.style.setProperty('--value', value + '%');
    sliderValue.textContent = radiusSlider.value;
}

radiusSlider.addEventListener('input', FillSlider);


FillSlider();
