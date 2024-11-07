//Re-name for each function
//Include general user-input validator

async function submitCalculation() {
    const operation = document.getElementById("operation").value;
    const dataInput = document.getElementById("data").value;
    
    // Parse the comma-separated input into an array of numbers
    //const data = dataInput.split(",").map(Number);
    const data = dataInput
        .split(",")
        .map(item => item.trim()) // Trim extra whitespace
        .filter(item => item !== "")
        .map(Number)
        .filter(value => !isNaN(value));          // Convert to number

    // Make sure the data is a valid array of numbers
    if ((data.some(isNaN)) || (data.length == 0)) {
        document.getElementById("result").textContent = "Please enter valid numbers separated by commas.";
        return;
    }

    // Send request to FastAPI based on the selected operation
    let url = "";
    let requestData = {};

    if (operation === "standard_deviation") {
        url = "/calculate_standard_deviation";
        requestData = { data };
    }

    try {
        console.log(data);
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(requestData),
        });

        // Parse response and display result
        const result = await response.json();
        document.getElementById("result").textContent = result?.standard_deviation ?? "Error";
        //document.getElementById("result").textContent = result.standard_deviation || console.log(data);
    } catch (error) {
        document.getElementById("result").textContent = "An error occurred.";
    }
}