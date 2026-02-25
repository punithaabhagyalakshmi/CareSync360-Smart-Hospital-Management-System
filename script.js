// =====================================
// RUN WHEN PAGE LOADS
// =====================================

document.addEventListener("DOMContentLoaded", function () {
    updateClock();
    highlightActivePatient();
    scrollToActive();
    checkEmergency();
});


// =====================================
// LIVE DIGITAL CLOCK
// =====================================

function updateClock() {
    const clock = document.getElementById("clock");
    if (!clock) return;

    function refreshTime() {
        const now = new Date();
        clock.innerText = now.toLocaleTimeString();
    }

    refreshTime();
    setInterval(refreshTime, 1000);
}


// =====================================
// SEARCH PATIENT
// =====================================

function searchPatient() {
    const input = document.getElementById("searchInput");
    if (!input) return;

    const filter = input.value.toLowerCase();
    const rows = document.querySelectorAll("#patientTable tbody tr");

    rows.forEach(row => {
        const text = row.innerText.toLowerCase();
        row.style.display = text.includes(filter) ? "" : "none";
    });
}


// =====================================
// FILTER BY DEPARTMENT
// =====================================

function filterDepartment() {
    const select = document.getElementById("deptFilter");
    if (!select) return;

    const selected = select.value;
    const rows = document.querySelectorAll("#patientTable tbody tr");

    rows.forEach(row => {
        const deptCell = row.cells[3]; // Department column
        if (!deptCell) return;

        const dept = deptCell.innerText.trim();

        if (selected === "All" || dept === selected) {
            row.style.display = "";
        } else {
            row.style.display = "none";
        }
    });
}


// =====================================
// DARK / LIGHT MODE TOGGLE
// =====================================

function toggleMode() {
    document.body.classList.toggle("light-mode");
}


// =====================================
// HIGHLIGHT ACTIVE CONSULTATION
// =====================================

function highlightActivePatient() {
    const rows = document.querySelectorAll("#patientTable tbody tr");

    rows.forEach(row => {
        row.style.boxShadow = "none"; // reset first

        const statusBadge = row.querySelector(".badge");
        if (!statusBadge) return;

        if (statusBadge.innerText.includes("In Consultation")) {
            row.style.boxShadow = "0 0 18px #2196f3";
            row.style.transition = "0.3s ease";
            row.style.transform = "scale(1.01)";
        }
    });
}


// =====================================
// AUTO SCROLL TO ACTIVE PATIENT
// =====================================

function scrollToActive() {
    const rows = document.querySelectorAll("#patientTable tbody tr");

    rows.forEach(row => {
        const statusBadge = row.querySelector(".badge");
        if (!statusBadge) return;

        if (statusBadge.innerText.includes("In Consultation")) {
            row.scrollIntoView({
                behavior: "smooth",
                block: "center"
            });
        }
    });
}


// =====================================
// EMERGENCY ALERT DETECTION
// =====================================

let emergencyAlertShown = false;

// =====================================
// EMERGENCY ALERT DETECTION (FIXED)
// =====================================

function checkEmergency() {
    const rows = document.querySelectorAll("#patientTable tbody tr");

    let emergencyActive = false;

    rows.forEach(row => {
        const priorityCell = row.cells[4];   // Priority column
        const statusBadge = row.querySelector(".badge");  // Status column

        if (!priorityCell || !statusBadge) return;

        if (
            priorityCell.innerText.includes("Emergency") &&
            statusBadge.innerText.includes("Waiting")
        ) {
            emergencyActive = true;
        }
    });

    if (emergencyActive) {
        alert("🚨 Emergency Patient Waiting!");
    }
}