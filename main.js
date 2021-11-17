function draw_js(height, width, color) {
    var shap = document.getElementById('shap')
    shap.style.height = height + "px"
    shap.style.width = width + "px"
    shap.style.backgroundColor = color
    shap.style.borderRadius = "5px"
}

function draw_js_2() {
    var height = parseInt(document.getElementById('height2').value)
    var width = parseInt(document.getElementById('width2').value)
    var color = document.getElementById('color2').value
    draw_br_2(height, width, color)
}