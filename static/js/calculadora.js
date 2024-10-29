document.addEventListener('DOMContentLoaded', function() {
    form_carbon_footprint = document.getElementById('form-carbon-footprint');
    form_carbon_footprint.addEventListener('submit', function(event) {
        event.preventDefault();
        calculateCarbonFootprint()
    });
});

function calculateCarbonFootprint() {
            const carEmissionFactor = 0.2; // kg CO2/km en vehículo privado
            const publicTransportEmissionFactor = 0.08; // kg CO2/km en transporte público
            const electricityEmissionFactor = 0.55; // kg CO2/kWh (depende del mix energético del país)
            const gasEmissionFactor = 2; // kg CO2/m³ de gas natural
            const meatEmissionFactor = 10; // kg CO2/consumo semanal de carne
            const waterEmissionFactor = 0.5; // kg CO2/litro de agua

            const carKm = parseFloat(document.getElementById('carKm').value) || 0;
            const publicKm = parseFloat(document.getElementById('publicKm').value) || 0;
            const electricity = parseFloat(document.getElementById('electricity').value) || 0;
            const gas = parseFloat(document.getElementById('gas').value) || 0;
            const meat = parseFloat(document.getElementById('meat').value) || 0;
            const water = parseFloat(document.getElementById('water').value) || 0;

            const carEmissions = carKm * carEmissionFactor * 12;
            const publicTransportEmissions = publicKm * publicTransportEmissionFactor * 12;
            const electricityEmissions = electricity * electricityEmissionFactor * 12;
            const gasEmissions = gas * gasEmissionFactor * 12;
            const meatEmissions = meat * meatEmissionFactor * 52; // Consumo semanal
            const waterEmissions = water * waterEmissionFactor * 365;

            const totalEmissions = carEmissions + publicTransportEmissions + electricityEmissions + gasEmissions + meatEmissions + waterEmissions;

            document.getElementById('carbonFootprint').innerHTML = totalEmissions.toFixed(2);


            const data = {
                carEmissions: carEmissions,
                publicTransportEmissions: publicTransportEmissions,
                electricityEmissions: electricityEmissions,
                gasEmissions: gasEmissions,
                meatEmissions: meatEmissions,
                waterEmissions: waterEmissions,
                totalEmissions: totalEmissions
            };

            // Send data to the Flask endpoint
            fetch('/save_carbon_footprint', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
            .then(response => response.blob())
            .then(blob => {
                
                const imgUrl = URL.createObjectURL(blob);
                const imgElement = document.getElementById('chartImage');
                imgElement.src = imgUrl;
                imgElement.style.display = 'block';
                document.getElementById('resultFootprint').style.display = 'block';
            })
            .catch((error) => {
                console.error('Error:', error);
            });
}