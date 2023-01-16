$(document).ready(function() {
  $.get("/firewall_rules/", function(data) {
    data.forEach(function(rule) {
      $("

$(document).ready(function() {
  $("#rule-form").submit(function(event) {
    event.preventDefault();
    var ruleName = $("#rule-name").val();
    var rule = $("#rule").val();

    // Add a new row to the table with the new firewall rule data
    $("#rules-table tbody").append(
      "<tr>" +
        "<td>" + ruleName + "</td>" +
        "<td>" + rule + "</td>" +
        "<td>" +
          "<button class='btn btn-danger delete-rule'>Delete</button>" +
          "<button class='btn btn-info modify-rule'>Modify</button>" +
        "</td>" +
      "</tr>"
    );
  });
});

// Clear NAT rules button event listener
document.getElementById("clear-nat-rules-button").addEventListener("click", function(event) {
  event.preventDefault();
  // Clear NAT rules code here
  // This can be done by sending a DELETE request to the server to delete all NAT rules in the database
});


$.ajax({
    type: 'GET',
    url: '/get_firewall_rules',
    success: function(data) {
        // Parse the firewall rules and update the table
        var rules = JSON.parse(data);
        for (var i = 0; i < rules.length; i++) {
            $('#rules-table > tbody:last-child').append(
                '<tr><td>' + rules[i].name + '</td><td>' + rules[i].rule + '</td></tr>'
            );
        }
    }