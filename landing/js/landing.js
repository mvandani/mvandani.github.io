var datasets = [{
	title: 'Monthly milk production: pounds per cow. Jan 62 - Dec 75',
	sourceUrl: 'https://datamarket.com/data/set/22ox/monthly-milk-production-pounds-per-cow-jan-62-dec-75',
	url: 'landing/data/monthly-milk-production-pounds-p.csv'
}, {
	title: 'Price of chicken, 1924-1993, in constant $',
	sourceUrl: 'https://datamarket.com/data/set/22l9/price-of-chicken-1924-1993-in-constant',
	url: 'landing/data/price-of-chicken-19241993-in-con.csv'
}, {
	title: 'Wolfer sunspot numbers, 1770 to 1869',
	sourceUrl: 'https://datamarket.com/data/set/22wh/wolfer-sunspot-numbers-1770-to-1869',
	url: 'landing/data/wolfer-sunspot-numbers-1770-to-1.csv'
}, {
	title: 'Money stock, U.S., 1889 to 1970',
	sourceUrl: 'https://datamarket.com/data/set/22so/money-stock-us-1889-to-1970',
	url: 'landing/data/money-stock-us-1889-to-1970.csv'
}];

var dataset = datasets[Math.floor(Math.random() * datasets.length)];
var data, xScale, yScale, width, height;

function loadDataset(anythingButThisDataset) {
	var index = datasets.indexOf(dataset) + 1;
	if(index > datasets.length - 1)
		index = 0;
	dataset = datasets[index];
	d3.csv(dataset.url, function(d) {
		var keys = Object.keys(d);
		return {
			date: new Date(d[keys[0]]),
			value: +d[keys[1]]
		}
	}, function(error, rows) {
		data = rows;
		redrawChart(true);
		window.addEventListener('resize', function(event) {
	    	redrawChart(false);
		}, false);		
	});
	document.getElementById("source-url").innerHTML = dataset.title;
	document.getElementById("source-url").href = dataset.sourceUrl;
	window.scrollTo(0, 0);
}

function redrawChart(animate) {
	width = parseInt(d3.select("#chart").style("width"));
	height = parseInt(d3.select("#chart").style("height"));
	
	xScale = d3.scale.linear()
		.domain(d3.extent(data, function(d) { return d.date; }))
		.range([0, width]);
	yScale = d3.scale.linear()
		.domain(d3.extent(data, function(d) { return d.value; }))
		.range([height * 0, height * .50]);

   var line = d3.svg.area()
    	.x(function(d) { return xScale(d.date); })
    	.y0(height)
    	.y1(function(d) { return height - yScale(d.value); });

	var svg = d3.selectAll("svg")
    	.attr("width", width)
    	.attr("height", height);
    svg.html();
    svg.selectAll("*").remove();

    var totalLength = data.length;
    var path = svg.append("path")
    	.datum(data)
		.attr("class", "line")
		.attr("d", line);
}

loadDataset();