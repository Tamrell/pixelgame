
//Array class extension with function extend, functions like python extend
Array.prototype.extend = function (other_array) {
    /* You should include a test to check whether other_array really is an array */
    other_array.forEach(function(v) {this.push(v)}, this);
}

var classcount = 0
var alpha = "abcdefghijklmnopqrstuvwxyz"
var sheet = document.getElementById('pixelclasses').sheet
var sheet2 = document.createElement('style')
sheet2.type = 'text/css';
var class_info = create_classes();
var SUBIMAGE_COLORS = class_info[1];

sheet2.innerHTML = class_info[0];
var first = true;
var clickcount = 0;
var date = new Date();
date.setTime(date.getTime() + (10 * 24 * 60 * 60 * 1000));
var expires = "; expires=" + date.toGMTString();

document.getElementsByTagName('head')[0].appendChild(sheet2);

var classNames = Array.apply(null, Array(20)).map(function (_, i) {return alpha[i]+i;});

// https://stackoverflow.com/questions/1374126/how-to-extend-an-existing-javascript-array-with-another-array-without-creating/17368101#17368101


function ajax_save(choice) {
    if (window.XMLHttpRequest) {
        // code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp = new XMLHttpRequest();
    } else {
        // code for IE6, IE5
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }


    var sendstring = ""
    var all_imgs = [];
    for (var j = 0; j<9; j++){
        all_imgs.push(JSON.stringify(SUBIMAGE_COLORS[alpha[j]]));
    }
    var fields = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "imgchoice","choicenumbr"];
    var field_vals = [];
    for (var j = 0; j<all_imgs.length;j++){
        field_vals.push(all_imgs[j]);
    }
    field_vals.push(choice);
    field_vals.push(clickcount.toString());
    for (var j = 0; j < fields.length - 1; j++) {
        sendstring = sendstring.concat(fields[j] + "=" + field_vals[j] + "&");
    }
    var j = fields.length - 1;
    sendstring = sendstring.concat(fields[j] + "=" + field_vals[j]);

    xmlhttp.open("POST","pixelsave.php?");
    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

    xmlhttp.send(sendstring);
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            this.responseText;
        }
    };
}



function generate_subimages_from_example(example){
    if(first){
        document.getElementById('e').removeAttribute("onclick");
    }
    var example_colors=SUBIMAGE_COLORS[example];
    var all_classes = Array();
    var img_colors = Array();
    for (var j = 0; j < 4; j++){
        classnames_subimage = Array.apply(null, Array(64)).map(function (_, i) {return [alpha[j]+i, i];});
        subimage_info = classnames_subimage.map(function(v) {return create_class_from_example(v[0], example_colors[v[1]]);});
        subimage_classes = subimage_info.map(function(v) {return v[0]});
        subimage_colors = subimage_info.map(function(v) {return v[1]});
        img_colors[alpha[j]] = subimage_colors;
        all_classes.extend(subimage_classes);
    };

    classnames_subimage = Array.apply(null, Array(64)).map(function (_, i) {return [alpha[4]+i, i];})

    subimage_info = classnames_subimage.map(function(v) {return make_colorclass(v[0], example_colors[v[1]])});
    subimage_classes = subimage_info.map(function(v) {return v[0]});
    subimage_colors = subimage_info.map(function(v) {return v[1]});
    img_colors[alpha[4]] = subimage_colors;
    all_classes.extend(subimage_classes);

    for (var j = 5; j < 9; j++){
        classnames_subimage = Array.apply(null, Array(64)).map(function (_, i) {return [alpha[j]+i, i];});
        subimage_info = classnames_subimage.map(function(v) {return create_class_from_example(v[0], example_colors[v[1]])});
        subimage_classes = subimage_info.map(function(v) {return v[0]});
        subimage_colors = subimage_info.map(function(v) {return v[1]});
        img_colors[alpha[j]] = subimage_colors;
        all_classes.extend(subimage_classes);
    };
    sheet2.innerHTML = all_classes.join(" ");
    SUBIMAGE_COLORS = img_colors;
}

function mutate_color(oc, randrate){
    var r = parseInt(oc.slice(1,3), 16);
    var g = parseInt(oc.slice(3,5), 16);
    var b = parseInt(oc.slice(5,7), 16);

    r += Math.round((Math.random()*2-1)*randrate);
    g += Math.round((Math.random()*2-1)*randrate);
    b += Math.round((Math.random()*2-1)*randrate);

    r = Math.max(Math.min(r, 255), 0);
    g = Math.max(Math.min(g, 255), 0);
    b = Math.max(Math.min(b, 255), 0);

    var new_col = pad_hex(r,g,b);
    return new_col;
}

function pad_color(color_value){
    var hex = color_value.toString(16);
    try {
        hex = "0".repeat(2-hex.length) + hex;
    } catch {
        if (color_value > 250) {
            console.log(color_value.toString(), hex, hex.length.toString(), 2-hex.length);
        }
    }
    return hex;
}

function pad_hex(r,g,b){
    padded = [r,g,b].map(pad_color);
    return "#" + padded.join("");
}

function make_colorclass(classname, original_color){
    var style = '.' + classname + ' {';
    style += 'background-color:' + original_color +';';
    style += '}';
    return [style, original_color];
}

function create_class_from_example(classname, original_color){
    new_color = mutate_color(original_color, 40);
    var style = '.' + classname + ' {';
    style += 'background-color:' + new_color +';';
    style += '}';
    return [style, new_color];
}

function create_class(classname){
	var style = '.' + classname + ' {';
    var col = get_rand_color();
	style += 'background-color:' + col +';';
	style += '}';
    return [style, col];
}

function create_classes(){
    var all_classes = Array();
    var img_colors = Array();
    for (var j = 0; j < 9; j++) {
        classnames_subimage = Array.apply(null, Array(64)).map(function (_, i) {return alpha[j]+i;})
        subimage_info = classnames_subimage.map(create_class);
        subimage_classes = subimage_info.map(function(v) {return v[0]});
        subimage_colors = subimage_info.map(function(v) {return v[1]});
        img_colors[alpha[j]] = subimage_colors;
        all_classes.extend(subimage_classes);
    };
    return [all_classes.join(" "), img_colors]
}


function get_rand_color(){
	// check if understand = difficult: https://www.paulirish.com/2009/random-hex-color-code-snippets/
	return '#'+Math.floor(Math.random()*16777215).toString(16);
}


function pixelsclicked(choice){
    if (clickcount < 49){
        ajax_save(choice);
        generate_subimages_from_example(choice);
        clickcount++;
        //var l = <?php imgsubmit();?>
    } else {
        ajax_save(choice);
        window.location.href = "./survey_page.php";
    }
    //alert("does actually work");
}
