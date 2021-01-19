var margin = {top: 20, right: 20, bottom: 70, left: 40},
    width = 600 - margin.left - margin.right,
    height = 300 - margin.top - margin.bottom;
 
 
// set the ranges
var x = d3.scale.ordinal().rangeRoundBands([0, width], .05);
 
var y = d3.scale.linear().range([height, 0]);
 
// define the axis
var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom")
 
 
var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left")
    .ticks(10);
 
 
// add the SVG element
var svg2 = d3.select("#graficos").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");
 
 
// load the data from SlashDB via a RESTful API to the resource for the SQL Pass-thru (query)
d3.json("https://demo.slashdb.com/query/sales-by-year.json", function(error, data) {
 
    data.forEach(function(d) {
        d.Year = d.Year;
        d.Total = +d.Total;
    });
 
  // scale the range of the data
  x.domain(data.map(function(d) { return d.Year; }));
  y.domain([0, d3.max(data, function(d) { return d.Total; })]);
 
  // add axis
  svg2.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis)
      .selectAll("text")
      .style("text-anchor", "end")
      .attr("dx", "-.8em")
      .attr("dy", "-.55em")
      .attr("transform", "rotate(-90)" );
 
  svg2.append("g")
      .attr("class", "y axis")
      .call(yAxis)
      .append("text")
      .attr("y", -16)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Total Ventas");
 
 
  // Add bar chart
  svg2.selectAll("bar")
      .data(data)
    .enter().append("rect")
      .attr("class", "bar")
      .attr("x", function(d) { return x(d.Year); })
      .attr("width", x.rangeBand() - 20)
      .attr("y", function(d) { return y(d.Total); })
      .attr("height", function(d) { return height - y(d.Total); });
 
});