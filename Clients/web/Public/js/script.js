// IIFE - Immediately Invoked Function Expression
(function($, window, document) {

// The $ is now locally scoped 

// Listen for the jQuery ready event on the document
$(function() {

// The DOM is ready!

// initiate modal state
$('#myModal').modal('hide');

$( "#blockHeaderInfo" ).submit(function( event ) {
	event.preventDefault();

	// get values from form
	var data = {};
	$.each($(this).serializeArray(), function(i, field) {
	    data[field.name] = field.value;
	});
	// get hash
	$.ajax({ 
		url: "/api/hash", 
		data: data,
		dataType: 'json',
		success: function( data ) {
			$('.hash-value').text(data.hash)
			$('#myModal').modal('show')
		}
	});
});
});

// The rest of the code goes here!

}(window.jQuery, window, document));
// The global jQuery object is passed as a parameter
