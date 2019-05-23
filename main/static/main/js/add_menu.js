let form = document.getElementsByClassName("multifield")[0].cloneNode(true);
let extras = document.getElementById("extras");
let total = document.getElementById("id_form-TOTAL_FORMS");

function addExtra() {
    form.innerHTML = form.innerHTML.replace(RegExp("-"+(total.value-1)+"-", 'g'), "-"+(total.value++)+"-");
    extras.append(form.cloneNode(true));
}


