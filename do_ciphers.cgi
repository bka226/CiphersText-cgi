#!/usr/bin/perl -wT
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);

my $text = param('text');


print header;
print start_html("The reverse of your text is ");

$text = reverse($text);
print <<EndHTML;
<center>
<p>The reverse of your text is...</p>
<p>$text</p>
</center>
EndHTML

print end_html;
