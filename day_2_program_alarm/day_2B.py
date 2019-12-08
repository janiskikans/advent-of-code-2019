# Read opcodes from input file to list of ints
def read_opcodes_to_list():
    opcode_list = []
    file = open('input.txt', 'r')    

    for line in file.readlines():
        opcode_list = line.rstrip().split(',')
        
    for i in range(0, len(opcode_list)): 
        opcode_list[i] = int(opcode_list[i]) 

    return opcode_list

# Add two numbers
def add(number_1, number_2):
    return number_1 + number_2

# Multiply to numbers
def multiply(number_1, number_2):
    return number_1 * number_2

# Get the resulting opcode list
def get_opcode_output(opcode_list, input_1, input_2):
    current_opcode_position = 0
    opcode_list[1] = input_1
    opcode_list[2] = input_2
    
    while (current_opcode_position < len(opcode_list)):
        current_opcode_value = opcode_list[current_opcode_position]
        first_input_value = opcode_list[opcode_list[current_opcode_position + 1]]
        second_input_value = opcode_list[opcode_list[current_opcode_position + 2]]
        result_position = opcode_list[current_opcode_position + 3]
        
        if (current_opcode_value == 1):
            opcode_list[result_position] = add(first_input_value, second_input_value)
        
        if (current_opcode_value == 2):
            opcode_list[result_position] = multiply(first_input_value, second_input_value)
            
        if (opcode_list[current_opcode_position + 4] == 99):
            print('* HALT...')
            break
        
        current_opcode_position += 4
    
    return opcode_list
        
# Guess the pair of inputs that give the wanted result
def guess_correct_input_pair(wanted_output):
    opcode_result_list = []
    output = 0
    noun = 0
    verb = 0
    
    for noun in range(0, 99):
        for verb in range(0,99):
            opcode_list = read_opcodes_to_list()
            opcode_result_list = get_opcode_output(opcode_list, noun, verb)
            output = opcode_result_list[0]
        
            print(output)
        
            if (output >= wanted_output):
                break
        
        if (output >= wanted_output):
            print("\nMATCHING RESULT FOUND!")
            break
    
    print("--------------------")
    print("Result: " + str(output))
    print("Noun: " + str(noun))
    print("Verb: " + str(verb))
    print("Answer: " + str(calculate_answer(noun, verb)))
    print("--------------------")
    
# Get the correct task answer
def calculate_answer(noun, verb):
    return 100 * noun + verb

if __name__ == '__main__':
    guess_correct_input_pair(19690720)
    