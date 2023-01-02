function updateStatus(newStatus){
    const element = document.getElementById("status");
    element.innerHTML = newStatus;
}

updateStatus("Status: Good");