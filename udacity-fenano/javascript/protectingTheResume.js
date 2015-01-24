var html =
	'<script src="http://hackyourwebsite.com/eviljavascript.js"></script>';

var charEscape = function(_html) {
	var newHTML = _html;
	// Make sure that newHTML doesn't contain any < or > by replacing with character entity references

	newHTML = _html.replace(/</g, "&lt;");
	newHTML = newHTML.replace(/>/g, "&lt;");

	return newHTML;
};

// Did your code work? The line below will tell you!
console.log(charEscape(html));
