#!/usr/bin/ruby

puts ARGV

d = File.dirname(ARGV[0]) + '/'
text = File.read(ARGV[0])
replaced = text.gsub(/^% import-script (.*)$/) {|match|
	'[[[' + "\n" + File.read(d + $1) + "\n" + ']]]' + "\n"
}

File.open(ARGV[0], 'w') {|f| f.write(replaced) }
