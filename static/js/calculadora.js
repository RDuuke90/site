function calculateCarbonFootprint() {
            const carEmissionFactor = 0.2; // kg CO2/km en vehículo privado
            const publicTransportEmissionFactor = 0.08; // kg CO2/km en transporte público
            const electricityEmissionFactor = 0.55; // kg CO2/kWh (depende del mix energético del país)
            const gasEmissionFactor = 2; // kg CO2/m³ de gas natural
            const meatEmissionFactor = 50; // kg CO2/consumo semanal de carne
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

            document.getElementById('result').innerHTML = `Tu huella de carbono es de aproximadamente <strong>${totalEmissions.toFixed(2)} kg de CO₂ al año</strong>.`;


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
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
                location.reload(); // Refresh the page to capture the new image
            })
            .catch((error) => {
                console.error('Error:', error);
            });
}