function checkDates() {
    var checkIn = document.getElementById('checkIn').value;
    var checkOut = document.getElementById('checkOut').value;

    var indate = new Date(checkIn);
    var outDate = new Date(checkOut)
    var currDate = new Date();

    if (indate < currDate) {
        alert('Choose a valid check in date');
        return false;
    } else if (outDate < indate) {
        alert('Check Out date cannot be before check in date');
        return false;
    }

}

let getNewElement = (function () {
    const idBase = 'my-unique-id-';
    let count = 0;
    return function (type = 'div') {
        let el = document.createElement(type);
        el.id = idBase + count;
        count += 1;
        return el;
    }
}());

function addRoom() {
    var roomRow = getNewElement("div");
    var colName = document.createElement("div");
    var colQty = document.createElement("div");
    var colCost = document.createElement("div");
    var colTotal = document.createElement("div");
    var colRemove = document.createElement("div");

    roomRow.classList.add("row");
    colName.classList.add("col-xl-3", "d-xl-flex", "justify-content-xl-center", "align-items-xl-center");
    colQty.classList.add("col-xl-2", "d-xl-flex", "justify-content-xl-center", "align-items-xl-center");
    colCost.classList.add("col-xl-3", "d-xl-flex", "justify-content-xl-center", "align-items-xl-center");
    colTotal.classList.add("col-xl-3", "d-xl-flex", "justify-content-xl-center", "align-items-xl-center");
    colRemove.classList.add("col-xl-1", "d-xl-flex", "justify-content-xl-center", "align-items-xl-center");

    var pName = document.createElement("input");
    var pQty = document.createElement("input");
    var pCost = document.createElement("input");
    var pTotal = document.createElement("input");
    var btnRemove = document.createElement("button");


    pName.setAttribute("type", "text");
    pName.setAttribute("form", "selectRoomForm");
    pName.setAttribute('readonly', true);
    pName.setAttribute("name", "roomName");
    pName.style.border = "none";
    pName.style.textAlign = "center";

    pQty.setAttribute("type", "text");
    pQty.setAttribute("form", "selectRoomForm");
    pQty.setAttribute('readonly', true);
    pQty.setAttribute("name", "roomQty");
    pQty.style.border = "none";
    pQty.style.textAlign = "center";

    pCost.setAttribute("type", "text");
    pCost.setAttribute('readonly', true);
    pCost.setAttribute("form", "selectRoomForm");
    pCost.setAttribute("name", "roomCost");
    pCost.style.border = "none";
    pCost.style.textAlign = "center";

    pTotal.setAttribute("type", "text");
    pTotal.setAttribute('readonly', true);
    pTotal.setAttribute("form", "selectRoomForm");
    pTotal.setAttribute("name", "roomTotal");
    pTotal.style.border = "none";
    pTotal.style.textAlign = "center";

    btnRemove.classList.add("btn", "btn-danger", "btn-sm", "removeDiv");
    btnRemove.setAttribute("onclick", "removeDiv(this)");
    btnRemove.style.marginRight = "2rem";



    var rooomName = String(document.getElementById("room-name").innerHTML);
    var qty = document.getElementById("roomQty").value;
    var cost = parseFloat(document.getElementById("roomCost").innerText);
    var total = cost * qty;


    if (qty == 0) {
        alert("select number of rooms");
    }
    else {
        pQty.value = "X " + String(qty);
        pCost.value = String(cost);
        pName.value = rooomName;
        pTotal.value = String(total);
        btnRemove.innerHTML = "REMOVE";

        var rooms = document.getElementById("addedRooms");

        rooms.appendChild(roomRow);
        roomRow.appendChild(colName);
        roomRow.appendChild(colQty);
        roomRow.appendChild(colCost);
        roomRow.appendChild(colTotal);
        roomRow.appendChild(colRemove);
        colName.appendChild(pName);
        colQty.appendChild(pQty);
        colCost.appendChild(pCost);
        colTotal.appendChild(pTotal);
        colRemove.appendChild(btnRemove);

        var btnConfirm = document.getElementById("btnConfirm");
        btnConfirm.disabled = false;


    }
}


function removeDiv(elem) {
    $(elem).parent('div').parent('div').remove();
}
