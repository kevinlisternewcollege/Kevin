def gcd (a,b):
    while b:
        a, b = b, a%b
    return a

def modfunction(a,b):

    nearest_value_to_a = int(int(a)/int(b))
    print ("Bobs encripted value^d", int(a))
    print ("Nearest value to Bob's encripted value",nearest_value_to_a*b)
    return int(a)-nearest_value_to_a*b


if __name__ == '__main__':

    Alices_1st_private_key = input ("Alice's first private key (hint best that you use 11) = ")
    Alices_2nd_private_key = input ("Alice's first private key (hint best that you use 17) = ")


    Alice_public_key = int(Alices_1st_private_key) * int(Alices_2nd_private_key)

    print ("\nAlice's public key for the whole world to see = ", Alice_public_key)

    p_value = int(Alices_1st_private_key) - 1
    q_value = int(Alices_2nd_private_key)-1

    pq = p_value * q_value

    print (f"Alice to needs to choose an number that is coprime to {pq}\n")

    Alices_second_number = input ("Alice's second number for all the world to see (hint use 7) = ")

    if gcd(pq,int(Alices_second_number)) == 1:
        print(f"The GCD with {pq} is 1 so you've made a good choice")
    else:
        print ("you had better change Alice's second choice. ")



    print ("\n Now it is Bob's turn to do some work ")

    Bobs_Character_to_send = input ("Bob's character to send (hint use X) = ")

    Bobs_Character_to_send_in_ASC_Code = int(ord(Bobs_Character_to_send)) #convert a character to ASCii code, you should know about this for the exam.

    print ("We change Bobs message to a numeric ASCii code, so it is now = ", Bobs_Character_to_send_in_ASC_Code)

    print ("\n We now encript Bobs message using C=(Bob's message in ASCii)^Alice's second choice (Mod Alices public key)")

    Bobs_encripted_message = (Bobs_Character_to_send_in_ASC_Code ** int(Alices_second_number)) % Alice_public_key

    print ("Bobs encripted message",Bobs_encripted_message)
    print (f"This is the secure value that Bob sends to Alice, \nit does not matter if anyone else intercepts this, they will not be able to find out it was {Bobs_Character_to_send}")

    print (f"\n Now Alice calculates a d_value")

    d_value  =(pq+1)/ gcd(7,pq+1) # this is the bit I have not yet got the maths working for a general case. But note that only Alice has the values of p and q
    print ("Alice's d_value =", d_value)

    print (f"\n Alice can now use the formula Message = Bobs encrypted value ^ d_value mod (Alices public key)")

    The_decoded_message = modfunction(Bobs_encripted_message ** int(Alices_second_number),
                                         Alice_public_key)

    print ("\n The ASCii code from Bob is = ", The_decoded_message)
    print ("And when converted into text it is = ",chr(The_decoded_message))