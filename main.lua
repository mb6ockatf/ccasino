#!/usr/bin/env lua

print = nil
local RULES = [[
casino game

rules:
- 1 to 18 or 19 to 36
- odd or even
- red, black or green
- any number from 0 to 36 and 00
print exclamation mark, quit or exit to finish game
]]

local entropy = 0

local function random(x, y)
    entropy = entropy + 1
	if x ~= nil and y == nil then
		y = x
		x = 1
	end
    if x ~= nil and y ~= nil then
		local seed = math.randomseed(os.time() + entropy)  ---@type integer
		local random_number = math.random(seed) * 999999 % y  ---@type float
        return math.floor(x + random_number)
    else
		local seed = math.randomseed(os.time() + entropy)
		returnmath.floor(math.random(seed) * 100)
    end
end

FG_COLORS = {default_fg = "\27[39m", black = "\27[30m",
dark_grey = "\27[90m", red = "\27[31m", light_red = "\27[91m",
green = "\27[32m", light_green = "\27[92m", orange = "\27[33m",
yellow = "\27[93m", blue = "\27[34m", light_blue = "\27[94m",
purple = "\27[35m", light_purple = "\27[95m", cyan = "\27[36m",
light_cyan = "\27[96m", light_gray = "\27[37m", white = "\27[97m"}

SPECIAL_STYLES = {bold = "\27[1m", nobold = "\27[22m",
underline = "\27[4m", nounderline = "\27[24m", negative = "\27[7m",
positive = "\27[27m"}

BG_COLORS = {nocolor = "\27[0m", bg_black = "\27[40m",
bg_red = "\27[41m", bg_green = "\27[42m", bg_yellow = "\27[43m",
bg_blue = "\27[44m", bg_magenta = "\27[45m", bg_cyan = "\27[46m",
bg_white = "\27[47m", default_bg = "\27[49m", bg_light_black = "\27[100m",  
bg_light_red = "\27[101m", bg_light_green = "\27[102m",
bg_light_yellow = "\27[103m", bg_light_blue = "\27[104m",
bg_light_magenta = "\27[105m", bg_light_cyan = "\27[106m",
bg_light_white = "\27[107m"}

local function set_fg_style(message, style)  ---@type string
	return FG_COLORS[style] .. message .. FG_COLORS.default_fg
end

local function set_special_style(message, style)  ---@type string
	local nostyle  ---@type string
	if style == "negative" then nostyle = "positive";
	else nostyle = "no" .. style; end
	return SPECIAL_STYLES[style] .. message .. SPECIAL_STYLES[nostyle]
end

local function set_special_bg(message, style)  ---@type string
	return BG_COLORS[style] .. message .. BG_COLORS.default_bg
end

local print_line = function(message) io.write(message .. "\n") end

local roulette = {}

function roulette.get_random_color()  ---@type string
	--[[probability of green cell is 2/38; red and black: 18/38 --]]
	local random_value = random(38)  ---@type integer
	if random_value > 36 then
		return "green"
	elseif random_value % 2 == 0 then
		return "black"
	end
	return "red"
end

function roulette.get_random_parity()  ---@type string
	local random_value = random(2)  ---@type integer
	if random_value == 2 then
		return "even"
	end
	return "odd"
end

function roulette.get_random_digit()  ---@type integer
	local random_value = random(38)  ---@type integer
	if random_value == 37 then random_value = 0;
	elseif random_value == 38 then random_value = "00"; end
	return tostring(random_value)
end

function roulette.get_random_range()
	if random(2) == 2 then
		return "19 to 36"
	end
	return "1 to 18"
end


local won, lost, length = 0, 0, 1  ---@type integer
local answer  ---@type string
local SEPARATOR = string.rep("-", 40)
io.write(RULES, "\n")
print_line(set_fg_style("turn " .. length, "light_blue"))
io.write("your choice: ")
local choice = io.read("*line"):lower()  ---@type string
choice = choice:lower()
while choice ~= "!" do
	if choice == "red" or choice == "black" or choice == "green" then
		answer = roulette.get_random_color()
	elseif choice == "odd" or choice == "even" then
		answer = roulette.get_random_parity()
	elseif choice == "1 to 18" or choice == "19 to 36" then
		answer = roulette.get_random_range()
	elseif choice == "!" or choice == "exit" or choice == "quit" then
		os.exit(0);
	elseif tonumber(choice) ~= nil then
		number_choice = tonumber(choice)
		if choice == "00" or 
			(0 <= number_choice and number_choice <= 36) then
			answer = roulette.get_random_digit()
		end
	end
	if answer == nil then
		print_line(set_fg_style("input value wasn't recongised", "red"))
	else
		print_line(set_fg_style("winning answer is " .. answer, "light_purple"))
	end
	length = length + 1
	print_line(SEPARATOR)
	print_line(set_fg_style("turn " .. length, "light_blue"))
	io.write("your choice: ")
	choice = io.read("*line"):lower()
	answer = nil
end