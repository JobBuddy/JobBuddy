//alert("Company js included")


//DATE-Picker
$('#datePicker').datepicker({
	format: 'dd/mm/yyyy',
	// todayHighlight:'TRUE',
	autoclose: true,
})

//JobTitle Autocompletion

var dataList = document.getElementById('jobTitle');
var input = document.getElementById('job_title');


var request = new XMLHttpRequest();

// Handle state changes for the request.
request.onreadystatechange = function(response) {
  if (request.readyState === 4) {
    if (request.status === 200) {
      // Parse the JSON
      var jsonOptions = JSON.parse(request.responseText);
      console.log(jsonOptions.array[0]);

      // Loop over the JSON array.
      jsonOptions.array.forEach(function(item) {
        // Create a new <option> element.
        var option = document.createElement('option');
        // Set the value using the item in the JSON array.
        option.value = item;
        // Add the <option> element to the <datalist>.
        dataList.appendChild(option);
      });

      // Update the placeholder text.
      input.placeholder = "UI/UX Designer";
    } else {
      // An error occured :(
      input.placeholder = "Couldn't load datalist options :(";
    }
  }
};

// Update the placeholder text.
input.placeholder = "Loading options...";

// Set up and make the request.
request.open('GET', './jobTitle.json', true);
request.send();