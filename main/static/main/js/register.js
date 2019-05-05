function user_type() {
    if (document.querySelector("#user_type select").value == "user") {
        document.getElementById("staff").classList.add("d-none");
    } else {
        document.getElementById("staff").classList.remove("d-none");
    }

}