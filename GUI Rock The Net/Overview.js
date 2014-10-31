	function fillTable(){
		
		var tbody = document.getElementById('myTable').getElementsByTagName('tbody')[0];
		
		var rules = [1,2,3,4,5,6,7,8,9,10];
		
		tbody.innerHTML = "";
		
		for(x = rules.length; x>0; x--){
			// Create an empty <tr> element and add it to the 1st position of the table:
			var row = tbody.insertRow(0);

			// Insert new cells (<td> elements) at the 1st and 2nd position of the "new" <tr> element:
			var cell1 = row.insertCell(0);
			var cell2 = row.insertCell(1);
			var cell3 = row.insertCell(2);
			var cell4 = row.insertCell(3);
			var cell5 = row.insertCell(4);
			
			var name = "test";
			var t2 = "test2";
			var t3 = "test2";
			var t4 = "test2";
			var traffic = '<Button class="btn btn-primary" onclick="printchart();">Traffic</Button>';
			
			// Add some text to the new cells:
			cell1.innerHTML = name;
			cell2.innerHTML = t2;
			cell3.innerHTML = t3;
			cell4.innerHTML = t4;
			cell5.innerHTML = traffic;
		}
	}

	
	function gochart() {

		var dps = []; // dataPoints

		var chart = new CanvasJS.Chart("chartContainer",{
			title :{
              text: "kb/s"
			},
			axisY: {
				includeZero: false
			},			
			data: [{
				type: "stepLine",
				markerSize: 0,
				dataPoints: dps 
			}]
		});

		var xVal = 0;
		var yVal = 100;	
		var updateInterval = 100;
		var dataLength = 100; // number of dataPoints visible at any point

		var updateChart = function (count) {
			count = count || 1;
			// count is number of times loop runs to generate random dataPoints.
			
			for (var j = 0; j < count; j++) {	
				yVal = yVal +  Math.round(3 + Math.random() *(-3-3));
				dps.push({
					x: xVal,
					y: yVal
				});
				xVal++;
			};
			if (dps.length > dataLength)
			{
				dps.shift();				
			}
			
			chart.render();		

		};
		
		var startChart = function (count) {
			count = count || 1;
			// count is number of times loop runs to generate random dataPoints.
			
			for (var j = 0; j < count; j++) {	
				yVal = null;
				dps.push({
					x: xVal,
					y: yVal
				});
				xVal++;
			};
			if (dps.length > dataLength)
			{
				dps.shift();				
			}
			
			chart.render();		

		};
		
		// generates first set of dataPoints
		startChart(dataLength); 

		// update chart after specified time. 
		setInterval(function(){updateChart()}, updateInterval); 

	}
	
	function printchart(){
		var chartdiv = document.getElementById('cvs');
		
		chartdiv.innerHTML = "";
		
		chartdiv.innerHTML = '<div id="chartContainer" style="height: 300px; width:100%;">';
		
		gochart();
	}