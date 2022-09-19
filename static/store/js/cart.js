// const addBtn = document.getElementById("add-button");
// const csrfmiddlewaretoken = document.querySelector(
// 	'input[name="csrfmiddlewaretoken"]'
// ).value;
// item_id = addBtn.value;

// Shopping Cart Ajax

$(document).on("click", "#add-button", function (e) {
	e.preventDefault();
	alert("clicked...");
	$.ajax({
		type: "POST",
		url: "{% url 'cart:cart_add' %}",
		data: {
			itemid: $("#add-button").val(),
			csrfmiddlewaretoken: "{{csrf_token}}",
			action: "post",
		},
		success: function (res) {},
		error: function (xhr, errmsg, err) {},
	});
});
