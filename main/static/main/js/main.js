// let navbar = new Vue({
//     el: '#navbar',
//     mounted: function () {
//         window.addEventListener("scroll", function () {
//             navbar.top = document.body.scrollTop;
//         });
//     },
//     data: {
//         top: 0,
//     },
//     computed: {
//     },
//     methods: {
//     }
// });


// let popup = new Vue({
//     el: '#popup',
//     data:{
//         isActive: true
//     },
//     methods: {
//         deactive: function() {
//             this.isActive = false;
//             document.body.className = "";
//         }
//     }
// }
// )


function deactive() {
    document.getElementById("popup").remove();
    document.body.className = "";
}

function voter(action, res_id) {
    document.getElementById("form").action = "/"+action+"_restaurants/";
    document.getElementById("res_id").value = res_id;
    document.getElementById("vote").click();
}

function equal() {
    let items = document.getElementsByClassName("equal")
    for (let item of items) {
        item.style.height = item.offsetWidth
    }
}

window.addEventListener("resize", equal)
equal()