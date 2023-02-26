import numpy as np
from PIL import Image
from js import document, console, Uint8Array, window, File, setInterval, setTimeout, clearInterval
from pyodide.ffi import create_proxy, create_once_callable
import pyodide.ffi.wrappers as wrappers
import base64
# import pyodide
import asyncio
import io
import json
import random
import pandas as pd
from html import unescape, escape
#import panel as pn  

# from bokeh import __version__
# from bokeh.document import Document
# from bokeh.embed.util import OutputDocumentFor, standalone_docs_json_and_render_items
# from bokeh.models import Slider, Div
# from bokeh.layouts import Row
# from bokeh.protocol.messages.patch_doc import process_document_events
#import coden
#import Hamming_code_test as hct
#import panel as pn

#Note: Functions for use in final product

window.sessionStorage.setItem("key1",json.dumps("1"))
# console.log(str(json.loads(window.sessionStorage.getItem("key1"))))
window.sessionStorage.setItem("key2",json.dumps("1"))
window.sessionStorage.setItem("key3",json.dumps("1"))

def callback1():
    variable1 = json.loads(window.sessionStorage.getItem("key1"))
    if variable1 == "1":
        Element("zero").write("o")       
        variable1 = json.dumps("2")
        window.sessionStorage.setItem("key1",variable1)
    elif variable1 == "2":
        Element("zero").write("n")
        variable1 = json.dumps("3")
        window.sessionStorage.setItem("key1",variable1)
    else:
        Element("zero").write("e")
        variable1 = json.dumps("1")
        window.sessionStorage.setItem("key1",variable1)

def callback2():
    variable2 = json.loads(window.sessionStorage.getItem("key2"))
    if variable2 == "1":
        Element("one").write("o")       
        variable2 = json.dumps("2")
        window.sessionStorage.setItem("key2",variable2)
    elif variable2 == "2":
        Element("one").write("n")
        variable2 = json.dumps("3")
        window.sessionStorage.setItem("key2",variable2)
    else:
        Element("one").write("e")
        variable2 = json.dumps("1")
        window.sessionStorage.setItem("key2",variable2)

def callback3():
    variable3 = json.loads(window.sessionStorage.getItem("key3"))
    if variable3 == "1":
        Element("two").write("o")       
        variable3 = json.dumps("2")
        window.sessionStorage.setItem("key3",variable3)
    elif variable3 == "2":
        Element("two").write("n")
        variable3 = json.dumps("3")
        window.sessionStorage.setItem("key3",variable3)
    else:
        Element("two").write("e")
        variable3 = json.dumps("1")
        window.sessionStorage.setItem("key3",variable3)

async def text_appear(id):
    document.getElementById(id).style.visibility="visible"
    document.getElementById(id).className="animate glow"
    await asyncio.sleep(0)
    

def callback4():
    asyncio.ensure_future(text_appear('Title_text'))
    asyncio.ensure_future(text_appear('label'))
    asyncio.ensure_future(text_appear('Title_text2'))

def callback5():
    Element("zero").write("o")

def callback6():
    Element("one").write("n")

def callback7():
    Element("two").write("e")
    

setInterval_1 = setInterval(create_proxy(callback1), 75)
setInterval_2 = setInterval(create_proxy(callback2), 100)
setInterval_3 = setInterval(create_proxy(callback3), 125)
_1 = setTimeout(create_once_callable(lambda: clearInterval(setInterval_1)),3900)
_2 = setTimeout(create_once_callable(lambda: clearInterval(setInterval_2)),5300)
_3 = setTimeout(create_once_callable(lambda: clearInterval(setInterval_3)),6750)
_4 = setTimeout(create_proxy(callback5),4000)
_5 = setTimeout(create_proxy(callback6),5400)
_6 = setTimeout(create_proxy(callback7),6900)
_7 = setTimeout(create_proxy(callback4),7000)

def loading(nothing):
    document.getElementById("loading_ani").classList.add('lds-facebook')

upload_file = create_proxy(loading)
document.getElementById("file-upload").addEventListener("change", upload_file)
# print("website_title loaded")

class ReedSolomonError(Exception):
    pass

# Converts a binary list of 8 or less into binary array
def convLToA(list):
    array = np.zeros(8)
    if len(list) < 8:
        array[8 - len(list):8] = list
        return np.array(array)
    else:
        array[0:8] = list
        return np.array(array)

def convertFinite(Ham_signal, mod):
    copy = Ham_signal.copy()
    if len(np.shape(Ham_signal)) == 2:
        x,y = np.shape(Ham_signal)
        for i in range(0, x):
            for j in range(0,y):
                copy[i][j] = Ham_signal[i][j] % mod
        return copy
    else:
        for i in range(0,len(Ham_signal)):
            copy[i] = Ham_signal[i] % mod
        return copy

#ToDo: Function for conversion from image to binary array
async def imageToBinary(img):
    img = img.convert('L')
    # print('convert to greyscale')
    # print(img)
    img = np.array(img)
    # print('convert numpy')
    x,y = np.shape(img)
    # print(x,y)
    for i in range(0,x):
        for j in range(0,y):
            if img[i][j] < 255/2:
                img[i][j] = 0
            else:
                img[i][j] = 1
    await asyncio.sleep(0)
    return img



#ToDo: Function for conversion from binary array to image

async def binaryToImage(numpy_2d):
    x,y = np.shape(numpy_2d)
    copy = numpy_2d.copy()
    for i in range(0,x):
        for j in range(0,y):
            if copy[i][j] == 1:
                copy[i][j] = 255
    await asyncio.sleep(0)
    copy = copy.astype(np.uint8)
    image = Image.fromarray(copy)
    image = image.convert('RGB')
    return image

#Note: Image_encode for hamming (7,4)
G = np.array([[1, 1, 0, 1],
              [1, 0, 1, 1],
              [1, 0, 0, 0],
              [0, 1, 1, 1],
              [0, 1, 0, 0],
              [0, 0, 1, 0],
              [0, 0, 0, 1]])
             

async def img_encode(img, message_length):
    x, y = np.shape(img)
    mod = y % message_length
    if mod != 0:
         for i in range(0, x):
             img[i].append(np.zeros(message_length - mod))
    
    harray = y/message_length + mod/message_length

    full_array = np.zeros((x,int(y + 3*harray)))
    console.log('starting encode')
    for i in range(0,x):
        for j in range(0, int(harray)):
            message = img[i][4*j:4*j+4]
            message = message.transpose()
            encoded = np.matmul(G, message)
            encoded = convertFinite(encoded, 2)
            full_array[i][7*j:7*j+7] = encoded
        if x % 30 == 0:
            await asyncio.sleep(0)
    console.log('exited img_encode')
    return full_array



#Note:  Must be in binary, so convert to binary

async def seperate_img(img,encoded_length, message_length):
    x,y = np.shape(img)
    copy2 = img.copy()
    p_s = y//encoded_length * message_length
    parity = encoded_length-message_length
    for i in range(0,x):
        for j in range(0,int(y/encoded_length)):
                copy2[i][message_length*j:message_length*j+message_length] = img[i][encoded_length*j:encoded_length*j+message_length]
                copy2[i][p_s+parity*j:p_s+parity*j+parity] = img[i][encoded_length*j+message_length:encoded_length*j+encoded_length]
        if x % 30 == 0:
            await asyncio.sleep(0)
    return copy2

async def seperate_img_hamming(img):
    x,y = np.shape(img)
    copy = img.copy()
    p_s = y//7 * 4
    for i in range(0,x):
        for j in range(0,y//7):
            copy[i][p_s + 3 * j] = img[i][7 * j]
            copy[i][p_s + 3 * j + 1] = img[i][7 * j + 1]
            copy[i][4 * j] = img[i][7 * j + 2]
            copy[i][p_s + 3 * j + 2] = img[i][7 * j + 3]
            copy[i][4 * j + 1] = img[i][7 * j + 4]
            copy[i][4 * j + 2] = img[i][7 * j + 5]
            copy[i][4 * j + 3] = img[i][7 * j + 6]
        if x % 30 == 0:
            await asyncio.sleep(0)
    return copy

async def rejoin_img_hamming(img):
    console.log('rejoin hamming img')
    x, y = np.shape(img)
    copy = img.copy()
    p_s = y // 7 * 4
    for i in range(0, x):
        for j in range(0, y // 7):
            copy[i][7 * j] = img[i][p_s + 3 * j]
            copy[i][7 * j + 1] = img[i][p_s + 3 * j + 1]
            copy[i][7 * j + 2] = img[i][4 * j]
            copy[i][7 * j + 3] = img[i][p_s + 3 * j + 2]
            copy[i][7 * j + 4] = img[i][4 * j + 1]
            copy[i][7 * j + 5] = img[i][4 * j + 2]
            copy[i][7 * j + 6] = img[i][4 * j + 3]
        if x % 30 == 0:
            await asyncio.sleep(0)
    return copy

H = np.array([[1, 0, 1, 0, 1, 0, 1],
              [0, 1, 1, 0, 0, 1, 1],
              [0, 0, 0, 1, 1, 1, 1]])

def errorPlace(bin):
    copy2 = bin.copy()
    syndrome = np.matmul(H,copy2)
    syndrome = convertFinite(syndrome, 2)
    string = '0b'
    for o in range(0,len(syndrome)):
        string = string + str(int(syndrome[len(syndrome)-1-o]))
    return int(string,2)

def errorCorrect(x):
    place = errorPlace(x)
    if place == 0:
        return x
    else:
        if x[place - 1] == 0:
            x[place - 1] = 1
        else:
            x[place - 1] = 0
        return x

async def correct_img_hamming(img):
    console.log('starting img correct')
    x,y = np.shape(img)
    copy2 = img.copy()
    for i in range(0,x):
        for j in range(0,y//7):
            mesg = img[i][7*j:7*j+7]
            cor_msg = errorCorrect(mesg)
            copy2[i][7 * j:7 * j + 7] = cor_msg
        if x % 30 == 0:
            await asyncio.sleep(0)
    console.log('img correct complete')
    return copy2



gf_exp = [0] * 512 #    Create list of 512 elements. In Python 2.6+, consider using bytearray
gf_log = [0] * 256

#Note: Section for reed solomon codes

def gf_mult_noLUT(x, y, prim=0):
    '''Multiplication in Galois Fields without using a precomputed look-up table (and thus it's slower)
    by using the standard carry-less multiplication + modular reduction using an irreducible prime polynomial'''

    ### Define bitwise carry-less operations as inner functions ###
    def cl_mult(x, y):
        '''Bitwise carry-less multiplication on integers'''
        z = 0
        i = 0
        while (y >> i) > 0:
            if y & (1 << i):
                z ^= x << i
            i += 1
        return z

    def bit_length(n):
        '''Compute the position of the most significant bit (1) of an integer. Equivalent to int.bit_length()'''
        bits = 0
        while n >> bits: bits += 1
        return bits

    def cl_div(dividend, divisor=None):
        '''Bitwise carry-less long division on integers and returns the remainder'''
        # Compute the position of the most significant bit for each integers
        dl1 = bit_length(dividend)
        dl2 = bit_length(divisor)
        # If the dividend is smaller than the divisor, just exit
        if dl1 < dl2:
            return dividend
        # Else, align the most significant 1 of the divisor to the most significant 1 of the dividend (by shifting the divisor)
        for i in range(dl1 - dl2, -1, -1):
            # Check that the dividend is divisible (useless for the first iteration but important for the next ones)
            if dividend & (1 << i + dl2 - 1):
                # If divisible, then shift the divisor to align the most significant bits and XOR (carry-less subtraction)
                dividend ^= divisor << i
        return dividend

    ### Main GF multiplication routine ###

    # Multiply the gf numbers
    result = cl_mult(x, y)
    # Then do a modular reduction (ie, remainder from the division) with an irreducible primitive polynomial so that it stays inside GF bounds
    if prim > 0:
        result = cl_div(result, prim)

    return result



def init_tables(prim=0x11d):
    '''Precompute the logarithm and anti-log tables for faster computation later, using the provided primitive polynomial.'''
    # prim is the primitive (binary) polynomial. Since it's a polynomial in the binary sense,
    # it's only in fact a single galois field value between 0 and 255, and not a list of gf values.
    global gf_exp, gf_log
    gf_exp = [0] * 512 # anti-log (exponential) table
    gf_log = [0] * 256 # log table
    # For each possible value in the galois field 2^8, we will pre-compute the logarithm a bv nd anti-logarithm (exponential) of this value
    x = 1
    for i in range(0, 255):
        gf_exp[i] = x # compute anti-log for this value and store it in a table
        gf_log[x] = i # compute log at the same time
        x = gf_mult_noLUT(x, 2, prim)

        # If you use only generator==2 or a power of 2, you can use the following which is faster than gf_mult_noLUT():
        #x <<= 1 # multiply by 2 (change 1 by another number y to multiply by a power of 2^y)
        #if x & 0x100: # similar to x >= 256, but a lot faster (because 0x100 == 256)
            #x ^= prim # substract the primary polynomial to the current value (instead of 255, so that we get a unique set made of coprime numbers), this is the core of the tables generation

    # Optimization: double the size of the anti-log table so that we don't need to mod 255 to
    # stay inside the bounds (because we will mainly use this table for the multiplication of two GF numbers, no more).
    for i in range(255, 512):
        gf_exp[i] = gf_exp[i - 255]
    return [gf_log, gf_exp]

init_tables()

def gf_add(x, y):
    return x ^ y


def gf_sub(x, y):
    return x ^ y  # in binary galois field, subtraction is just the same as addition (since we mod 2)

def gf_mul(x,y):
    if x==0 or y==0:
        return 0
    return gf_exp[(gf_log[x] + gf_log[y])%255] # should be gf_exp[(gf_log[x]+gf_log[y])%255] if gf_exp wasn't oversized

def gf_div(x,y):
    if y==0:
        raise ZeroDivisionError()
    if x==0:
        return 0
    return gf_exp[(gf_log[x] + 255 - gf_log[y]) % 255]

def gf_pow(x, power):
    return gf_exp[(gf_log[x] * power) % 255]

def gf_inverse(x):
    return gf_exp[255 - gf_log[x]] # gf_inverse(x) == gf_div(1, x)

def gf_poly_scale(p,x):
    r = [0] * len(p)
    for i in range(0, len(p)):
        r[i] = gf_mul(p[i], x)
    return r

def gf_poly_mul(p,q):
    '''Multiply two polynomials, inside Galois Field'''
    # Pre-allocate the result array
    r = [0] * (len(p)+len(q)-1)
    # Compute the polynomial multiplication (just like the outer product of two vectors,
    # we multiply each coefficients of p with all coefficients of q)
    for j in range(0, len(q)):
        for i in range(0, len(p)):
            r[i+j] ^= gf_mul(p[i], q[j]) # equivalent to: r[i + j] = gf_add(r[i+j], gf_mul(p[i], q[j]))
                                                         # -- you can see it's your usual polynomial multiplication
    return r

def rs_generator_poly(nsym):
    '''Generate an irreducible generator polynomial (necessary to encode a message into Reed-Solomon)'''
    g = [1]
    for i in range(0, nsym):
        g = gf_poly_mul(g, [1, gf_pow(2, i)])



    return g

def gf_poly_add(p,q):
    r = [0] * max(len(p),len(q))
    for i in range(0,len(p)):
        r[i+len(r)-len(p)] = p[i]
    for i in range(0,len(q)):
        r[i+len(r)-len(q)] ^= q[i]
    return r



def gf_poly_eval(poly, x):
    '''Evaluates a polynomial in GF(2^p) given the value for x. This is based on Horner's scheme for maximum efficiency.'''
    y = poly[0]
    for i in range(1, len(poly)):
        y = gf_mul(y, x) ^ poly[i]
    return y

def gf_poly_div(dividend, divisor):
    '''Fast polynomial division by using Extended Synthetic Division and optimized for GF(2^p) computations
    (doesn't work with standard polynomials outside of this galois field, see the Wikipedia article for generic algorithm).'''
    # CAUTION: this function expects polynomials to follow the opposite convention at decoding:
    # the terms must go from the biggest to lowest degree (while most other functions here expect
    # a list from lowest to biggest degree). eg: 1 + 2x + 5x^2 = [5, 2, 1], NOT [1, 2, 5]

    msg_out = list(dividend) # Copy the dividend
    #normalizer = divisor[0] # precomputing for performance
    for i in range(0, len(dividend) - (len(divisor)-1)):
        #msg_out[i] /= normalizer # for general polynomial division (when polynomials are non-monic), the usual way of using
                                  # synthetic division is to divide the divisor g(x) with its leading coefficient, but not needed here.
        coef = msg_out[i] # precaching
        if coef != 0: # log(0) is undefined, so we need to avoid that case explicitly (and it's also a good optimization).
            for j in range(1, len(divisor)): # in synthetic division, we always skip the first coefficient of the divisior,
                                              # because it's only used to normalize the dividend coefficient
                if divisor[j] != 0: # log(0) is undefined
                    msg_out[i + j] ^= gf_mul(divisor[j], coef) # equivalent to the more mathematically correct
                                                               # (but xoring directly is faster): msg_out[i + j] += -divisor[j] * coef
    # The resulting msg_out contains both the quotient and the remainder, the remainder being the size of the divisor
    # (the remainder has necessarily the same degree as the divisor -- not length but degree == length-1 -- since it's
    # what we couldn't divide from the dividend), so we compute the index where this separation is, and return the quotient and remainder.
    separator = -(len(divisor)-1)
    return msg_out[:separator], msg_out[separator:] # return quotient, remainder.

def rs_encode_msg(msg_in, nsym):
    '''Reed-Solomon main encoding function'''
    gen = rs_generator_poly(nsym)
    # Pad the message, then divide it by the irreducible generator polynomial
    _, remainder = gf_poly_div(msg_in + [0] * (len(gen)-1), gen)
    # The remainder is our RS code! Just append it to our original message to get our full codeword (this represents a polynomial of max 256 terms)
    msg_out = msg_in + remainder
    # Return the codeword
    return msg_out

def rs_calc_syndromes(msg, nsym):
    '''Given the received codeword msg and the number of error correcting symbols (nsym), computes the syndromes polynomial.
    Mathematically, it's essentially equivalent to a Fourrier Transform (Chien search being the inverse).
    '''
    # Note the "[0] +" : we add a 0 coefficient for the lowest degree (the constant). This effectively shifts the syndrome, and will shift every computations depending on the syndromes (such as the errors locator polynomial, errors evaluator polynomial, etc. but not the errors positions).
    # This is not necessary, you can adapt subsequent computations to start from 0 instead of skipping the first iteration (ie, the often seen range(1, n-k+1)),
    synd = [0] * nsym
    for i in range(0, nsym):
        synd[i] = gf_poly_eval(msg, gf_pow(2,i))
    return [0] + synd # pad with one 0 for mathematical precision (else we can end up with weird calculations sometimes)

def rs_check(msg, nsym):
    '''Returns true if the message + ecc has no error or false otherwise (may not always catch a wrong decoding or a wrong message, particularly if there are too many errors -- above the Singleton bound --, but it usually does)'''
    return (max(rs_calc_syndromes(msg, nsym)) == 0)

def rs_find_errata_locator(e_pos):
    '''Compute the erasures/errors/errata locator polynomial from the erasures/errors/errata positions
       (the positions must be relative to the x coefficient, eg: "hello worldxxxxxxxxx" is tampered to "h_ll_ worldxxxxxxxxx"
       with xxxxxxxxx being the ecc of length n-k=9, here the string positions are [1, 4], but the coefficients are reversed
       since the ecc characters are placed as the first coefficients of the polynomial, thus the coefficients of the
       erased characters are n-1 - [1, 4] = [18, 15] = erasures_loc to be specified as an argument.'''

    e_loc = [
        1]  # just to init because we will multiply, so it must be 1 so that the multiplication starts correctly without nulling any term
    # erasures_loc = product(1 - x*alpha**i) for i in erasures_pos and where alpha is the alpha chosen to evaluate polynomials.
    for i in e_pos:
        e_loc = gf_poly_mul(e_loc, gf_poly_add([1], [gf_pow(2, i), 0]))
    return e_loc

def rs_find_error_evaluator(synd, err_loc, nsym):
    '''Compute the error (or erasures if you supply sigma=erasures locator polynomial, or errata) evaluator polynomial Omega
       from the syndrome and the error/erasures/errata locator Sigma.'''

    # Omega(x) = [ Synd(x) * Error_loc(x) ] mod x^(n-k+1)
    _, remainder = gf_poly_div(gf_poly_mul(synd, err_loc),
                               ([1] + [0] * (nsym + 1)))  # first multiply syndromes * errata_locator, then do a
    # polynomial division to truncate the polynomial to the
    # required length

    # Faster way that is equivalent
    # remainder = gf_poly_mul(synd, err_loc) # first multiply the syndromes with the errata locator polynomial
    # remainder = remainder[len(remainder)-(nsym+1):] # then slice the list to truncate it (which represents the polynomial), which
    # is equivalent to dividing by a polynomial of the length we want

    return remainder

def rs_correct_errata(msg_in, synd, err_pos):  # err_pos is a list of the positions of the errors/erasures/errata
    '''Forney algorithm, computes the values (error magnitude) to correct the input message.'''
    # calculate errata locator polynomial to correct both errors and erasures (by combining the errors positions given by the error locator polynomial found by BM with the erasures positions given by caller)
    coef_pos = [len(msg_in) - 1 - p for p in
                err_pos]  # need to convert the positions to coefficients degrees for the errata locator algo to work (eg: instead of [0, 1, 2] it will become [len(msg)-1, len(msg)-2, len(msg) -3])
    err_loc = rs_find_errata_locator(coef_pos)
    # calculate errata evaluator polynomial (often called Omega or Gamma in academic papers)
    err_eval = rs_find_error_evaluator(synd[::-1], err_loc, len(err_loc) - 1)[::-1]

    # Second part of Chien search to get the error location polynomial X from the error positions in err_pos (the roots of the error locator polynomial, ie, where it evaluates to 0)
    X = []  # will store the position of the errors
    for i in range(0, len(coef_pos)):
        l = 255 - coef_pos[i]
        X.append(gf_pow(2, -l))

    # Forney algorithm: compute the magnitudes
    E = [0] * (
        len(msg_in))  # will store the values that need to be corrected (substracted) to the message containing errors. This is sometimes called the error magnitude polynomial.
    Xlength = len(X)
    for i, Xi in enumerate(X):

        Xi_inv = gf_inverse(Xi)

        # Compute the formal derivative of the error locator polynomial (see Blahut, Algebraic codes for data transmission, pp 196-197).
        # the formal derivative of the errata locator is used as the denominator of the Forney Algorithm, which simply says that the ith error value is given by error_evaluator(gf_inverse(Xi)) / error_locator_derivative(gf_inverse(Xi)). See Blahut, Algebraic codes for data transmission, pp 196-197.
        err_loc_prime_tmp = []
        for j in range(0, Xlength):
            if j != i:
                err_loc_prime_tmp.append(gf_sub(1, gf_mul(Xi_inv, X[j])))
        # compute the product, which is the denominator of the Forney algorithm (errata locator derivative)
        err_loc_prime = 1
        for coef in err_loc_prime_tmp:
            err_loc_prime = gf_mul(err_loc_prime, coef)
        # equivalent to: err_loc_prime = functools.reduce(gf_mul, err_loc_prime_tmp, 1)

        # Compute y (evaluation of the errata evaluator polynomial)
        # This is a more faithful translation of the theoretical equation contrary to the old forney method. Here it is an exact reproduction:
        # Yl = omega(Xl.inverse()) / prod(1 - Xj*Xl.inverse()) for j in len(X)
        y = gf_poly_eval(err_eval[::-1], Xi_inv)  # numerator of the Forney algorithm (errata evaluator evaluated)
        y = gf_mul(gf_pow(Xi, 1), y)

        # Check: err_loc_prime (the divisor) should not be zero.
        if err_loc_prime == 0:
            raise ReedSolomonError("Could not find error magnitude")  # Could not find error magnitude

        # Compute the magnitude
        magnitude = gf_div(y,
                           err_loc_prime)  # magnitude value of the error, calculated by the Forney algorithm (an equation in fact): dividing the errata evaluator with the errata locator derivative gives us the errata magnitude (ie, value to repair) the ith symbol
        E[err_pos[i]] = magnitude  # store the magnitude for this error into the magnitude polynomial

    # Apply the correction of values to get our message corrected! (note that the ecc bytes also gets corrected!)
    # (this isn't the Forney algorithm, we just apply the result of decoding here)
    msg_in = gf_poly_add(msg_in,
                         E)  # equivalent to Ci = Ri - Ei where Ci is the correct message, Ri the received (senseword) message, and Ei the errata magnitudes (minus is replaced by XOR since it's equivalent in GF(2^p)). So in fact here we substract from the received message the errors magnitude, which logically corrects the value to what it should be.
    return msg_in

def rs_find_error_locator(synd, nsym, erase_loc=None, erase_count=0):
    '''Find error/errata locator and evaluator polynomials with Berlekamp-Massey algorithm'''
    # The idea is that BM will iteratively estimate the error locator polynomial.
    # To do this, it will compute a Discrepancy term called Delta, which will tell us if the error locator polynomial needs an update or not
    # (hence why it's called discrepancy: it tells us when we are getting off board from the correct value).

    # Init the polynomials
    if erase_loc: # if the erasure locator polynomial is supplied, we init with its value, so that we include erasures in the final locator polynomial
        err_loc = list(erase_loc)
        old_loc = list(erase_loc)
    else:
        err_loc = [1] # This is the main variable we want to fill, also called Sigma in other notations or more formally the errors/errata locator polynomial.
        old_loc = [1] # BM is an iterative algorithm, and we need the errata locator polynomial of the previous iteration in order to update other necessary variables.
    #L = 0 # update flag variable, not needed here because we use an alternative equivalent way of checking if update is needed (but using the flag could potentially be faster depending on if using length(list) is taking linear time in your language, here in Python it's constant so it's as fast.

    # Fix the syndrome shifting: when computing the syndrome, some implementations may prepend a 0 coefficient for the lowest degree term (the constant). This is a case of syndrome shifting, thus the syndrome will be bigger than the number of ecc symbols (I don't know what purpose serves this shifting). If that's the case, then we need to account for the syndrome shifting when we use the syndrome such as inside BM, by skipping those prepended coefficients.
    # Another way to detect the shifting is to detect the 0 coefficients: by definition, a syndrome does not contain any 0 coefficient (except if there are no errors/erasures, in this case they are all 0). This however doesn't work with the modified Forney syndrome, which set to 0 the coefficients corresponding to erasures, leaving only the coefficients corresponding to errors.
    synd_shift = len(synd) - nsym

    for i in range(0, nsym-erase_count): # generally: nsym-erase_count == len(synd), except when you input a partial erase_loc and using the full syndrome instead of the Forney syndrome, in which case nsym-erase_count is more correct (len(synd) will fail badly with IndexError).
        if erase_loc: # if an erasures locator polynomial was provided to init the errors locator polynomial, then we must skip the FIRST erase_count iterations (not the last iterations, this is very important!)
            K = erase_count+i+synd_shift
        else: # if erasures locator is not provided, then either there's no erasures to account or we use the Forney syndromes, so we don't need to use erase_count nor erase_loc (the erasures have been trimmed out of the Forney syndromes).
            K = i+synd_shift

        # Compute the discrepancy Delta
        # Here is the close-to-the-books operation to compute the discrepancy Delta: it's a simple polynomial multiplication of error locator with the syndromes, and then we get the Kth element.
        #delta = gf_poly_mul(err_loc[::-1], synd)[K] # theoretically it should be gf_poly_add(synd[::-1], [1])[::-1] instead of just synd, but it seems it's not absolutely necessary to correctly decode.
        # But this can be optimized: since we only need the Kth element, we don't need to compute the polynomial multiplication for any other element but the Kth. Thus to optimize, we compute the polymul only at the item we need, skipping the rest (avoiding a nested loop, thus we are linear time instead of quadratic).
        # This optimization is actually described in several figures of the book "Algebraic codes for data transmission", Blahut, Richard E., 2003, Cambridge university press.
        delta = synd[K]
        for j in range(1, len(err_loc)):
            delta ^= gf_mul(err_loc[-(j+1)], synd[K - j]) # delta is also called discrepancy. Here we do a partial polynomial multiplication (ie, we compute the polynomial multiplication only for the term of degree K). Should be equivalent to brownanrs.polynomial.mul_at().
        #print "delta", K, delta, list(gf_poly_mul(err_loc[::-1], synd)) # debugline

        # Shift polynomials to compute the next degree
        old_loc = old_loc + [0]

        # Iteratively estimate the errata locator and evaluator polynomials
        if delta != 0: # Update only if there's a discrepancy
            if len(old_loc) > len(err_loc): # Rule B (rule A is implicitly defined because rule A just says that we skip any modification for this iteration)
            #if 2*L <= K+erase_count: # equivalent to len(old_loc) > len(err_loc), as long as L is correctly computed
                # Computing errata locator polynomial Sigma
                new_loc = gf_poly_scale(old_loc, delta)
                old_loc = gf_poly_scale(err_loc, gf_inverse(delta)) # effectively we are doing err_loc * 1/delta = err_loc // delta
                err_loc = new_loc
                # Update the update flag
                #L = K - L # the update flag L is tricky: in Blahut's schema, it's mandatory to use `L = K - L - erase_count` (and indeed in a previous draft of this function, if you forgot to do `- erase_count` it would lead to correcting only 2*(errors+erasures) <= (n-k) instead of 2*errors+erasures <= (n-k)), but in this latest draft, this will lead to a wrong decoding in some cases where it should correctly decode! Thus you should try with and without `- erase_count` to update L on your own implementation and see which one works OK without producing wrong decoding failures.

            # Update with the discrepancy
            err_loc = gf_poly_add(err_loc, gf_poly_scale(old_loc, delta))

    # Check if the result is correct, that there's not too many errors to correct
    while len(err_loc) and err_loc[0] == 0: del err_loc[0] # drop leading 0s, else errs will not be of the correct size
    errs = len(err_loc) - 1
    # if (errs-erase_count) * 2 + erase_count > nsym:
    #     raise ReedSolomonError("Too many errors to correct")    # too many errors to correct

    return err_loc

def rs_find_errors(err_loc, nmess):  # nmess is len(msg_in)
    '''Find the roots (ie, where evaluation = zero) of error polynomial by brute-force trial, this is a sort of Chien's search
    (but less efficient, Chien's search is a way to evaluate the polynomial such that each evaluation only takes constant time).'''
    errs = len(err_loc) - 1
    err_pos = []
    for i in range(
            nmess):  # normally we should try all 2^8 possible values, but here we optimize to just check the interesting symbols
        if gf_poly_eval(err_loc,
                        gf_pow(2, i)) == 0:  # It's a 0? Bingo, it's a root of the error locator polynomial,
            # in other terms this is the location of an error
            err_pos.append(nmess - 1 - i)
    # Sanity check: the number of errors/errata positions found should be exactly the same as the length of the errata locator polynomial
    # if len(err_pos) != errs:
    #     # couldn't find error locations
    #     raise ReedSolomonError("Too many (or few) errors found by Chien Search for the errata locator polynomial!")
    return err_pos

def rs_forney_syndromes(synd, pos, nmess):
    # Compute Forney syndromes, which computes a modified syndromes to compute only errors (erasures are trimmed out). Do not confuse this with Forney algorithm, which allows to correct the message based on the location of errors.
    erase_pos_reversed = [nmess - 1 - p for p in
                          pos]  # prepare the coefficient degree positions (instead of the erasures positions)

    # Optimized method, all operations are inlined
    fsynd = list(synd[1:])  # make a copy and trim the first coefficient which is always 0 by definition
    for i in range(0, len(pos)):
        x = gf_pow(2, erase_pos_reversed[i])
        for j in range(0, len(fsynd) - 1):
            fsynd[j] = gf_mul(fsynd[j], x) ^ fsynd[j + 1]

    # Equivalent, theoretical way of computing the modified Forney syndromes: fsynd = (erase_loc * synd) % x^(n-k)
    # See Shao, H. M., Truong, T. K., Deutsch, L. J., & Reed, I. S. (1986, April). A single chip VLSI Reed-Solomon decoder. In Acoustics, Speech, and Signal Processing, IEEE International Conference on ICASSP'86. (Vol. 11, pp. 2151-2154). IEEE.ISO 690
    # erase_loc = rs_find_errata_locator(erase_pos_reversed, generator=generator) # computing the erasures locator polynomial
    # fsynd = gf_poly_mul(erase_loc[::-1], synd[1:]) # then multiply with the syndrome to get the untrimmed forney syndrome
    # fsynd = fsynd[len(pos):] # then trim the first erase_pos coefficients which are useless. Seems to be not necessary, but this reduces the computation time later in BM (thus it's an optimization).

    return fsynd

def rs_correct_msg(msg_in, nsym, erase_pos=None):
    '''Reed-Solomon main decoding function'''
    if len(msg_in) > 255:  # can't decode, message is too big
        raise ValueError("Message is too long (%i when max is 255)" % len(msg_in))
        

    msg_out = list(msg_in)  # copy of message
    # erasures: set them to null bytes for easier decoding (but this is not necessary, they will be corrected anyway, but debugging will be easier with null bytes because the error locator polynomial values will only depend on the errors locations, not their values)
    if erase_pos is None:
        erase_pos = []
    else:
        for e_pos in erase_pos:
            msg_out[e_pos] = 0
    # check if there are too many erasures to correct (beyond the Singleton bound)
    if len(erase_pos) > nsym: raise ReedSolomonError("Too many erasures to correct")
    # prepare the syndrome polynomial using only errors (ie: errors = characters that were either replaced by null byte
    # or changed to another character, but we don't know their positions)
    synd = rs_calc_syndromes(msg_out, nsym)
    # check if there's any error/erasure in the input codeword. If not (all syndromes coefficients are 0), then just return the message as-is.
    if max(synd) == 0:
        return msg_out[:-nsym], msg_out[-nsym:]  # no errors

    # compute the Forney syndromes, which hide the erasures from the original syndrome (so that BM will just have to deal with errors, not erasures)
    fsynd = rs_forney_syndromes(synd, erase_pos, len(msg_out))
    # compute the error locator polynomial using Berlekamp-Massey
    err_loc = rs_find_error_locator(fsynd, nsym, erase_count=len(erase_pos))
    # locate the message errors using Chien search (or brute-force search)
    err_pos = rs_find_errors(err_loc[::-1], len(msg_out))
    # if err_pos is None:
    #     raise ReedSolomonError("Could not locate error")  # error location failed

    # Find errors values and apply them to correct the message
    # compute errata evaluator and errata magnitude polynomials, then correct errors and erasures
    msg_out = rs_correct_errata(msg_out, synd, (
                erase_pos + err_pos))  # note that we here use the original syndrome, not the forney syndrome
    # (because we will correct both errors and erasures, so we need the full syndrome)
    # check if the final message is fully repaired
    # synd = rs_calc_syndromes(msg_out, nsym)
    # if max(synd) > 0:
    #     raise ReedSolomonError("Could not correct message")  # message could not be repaired
    # return the successfully decoded message
    return msg_out[:-nsym], msg_out[-nsym:]  # also return the corrected ecc block so that the user can check()

#Note: https://users.math.msu.edu/users/halljo/classes/codenotes/Hamming.pdf

#Note: Put image through reed solomon processing

async def convertBintoRS(img_array, bit_grouping):
    copy = img_array.copy()

    x,y = np.shape(img_array)
    mod = y % bit_grouping
    if mod != 0:
        fresh = np.zeros((x,y+bit_grouping-mod))
        for i in range(0,x):
            for j in range(0,y):
                fresh[i][j] = copy[i][j]
    else:
        fresh = copy
    x,y = np.shape(fresh)
    y_2 = y // bit_grouping
    rs_array = np.zeros((x,y_2))
    for i in range(0, x):
        for j in range(0,y_2):
            bin = copy[i][bit_grouping*j:bit_grouping*j+bit_grouping]
            string = '0b'
            for a in range(0,len(bin)):
                string = string+str(int(bin[a]))
            rs_array[i][j] = int(string,2)
        if x % 30 == 0:
            await asyncio.sleep(0)
    return rs_array



#Note: Encode Message with Reed Solomon

async def encodeRS(rs_array,msg_len, error_c,prim=0x11d):
    x,y = np.shape(rs_array)
    total = msg_len+error_c
    new_array = np.zeros((x, y//msg_len * total))
    init_tables(prim)
    for i in range(0, x):
        for j in range(0,y//msg_len):
            msg = rs_array[i][msg_len*j:msg_len*j+msg_len]
            msg = msg.tolist()
            for k in range(0,len(msg)):
                msg[k] = int(msg[k])
            enc_msg = rs_encode_msg(msg,error_c)
            new_array[i][total*j:total*j+total] = np.array(enc_msg)
        if x % 30 == 0:
            await asyncio.sleep(0)
    return new_array



#Note: Shape is incorrect should be 180 instead of 280 (fixed)

#Note: Seperate image into image + parity (have function)


#Note: Need to make function to deconstruct reed solomon array back to binary

async def RStoBinary(rs_img_array, bit_length):
    x,y = np.shape(rs_img_array)
    fresh_arr = np.zeros((x,y*bit_length))
    for i in range(0,x):
        for j in range(0,y):
            number = rs_img_array[i][j]
            listv = list(bin(int(number)))
            listv = np.array(listv[2:len(listv)])
            listv = listv.astype(int)
            if len(listv) != bit_length:
                listv2 = np.zeros(8)
                listv2[len(listv2)-len(listv):len(listv2)] = listv
            else:
                listv2 = listv
            fresh_arr[i][bit_length*j:bit_length*j+bit_length] = listv2
        if x % 30 == 0:
            await asyncio.sleep(0)

    return fresh_arr

async def correctRS_img(rs_img_array,enc_msg_len,error_c,prim=0x11d):
    x, y = np.shape(rs_img_array)
    new_array = rs_img_array.copy()
    msg_len = enc_msg_len-error_c
    init_tables(prim) #Can we do this outside of this function to make it faster? Task for later
    fresh = np.zeros(enc_msg_len)
    for i in range(0, x):
        for j in range(0, y // enc_msg_len):
            msg = rs_img_array[i][enc_msg_len * j:enc_msg_len * j + enc_msg_len]
            msg = msg.tolist()
            for k in range(0, len(msg)):
                msg[k] = int(msg[k])
            correct_msg,parity = rs_correct_msg(msg,error_c)
            fresh[0:msg_len] = correct_msg
            fresh[msg_len:enc_msg_len] = parity
            new_array[i][enc_msg_len* j:enc_msg_len * j + enc_msg_len] = fresh
        if x % 30 == 0:
            await asyncio.sleep(0)
    return new_array

async def rejoin_img(img,encoded_length, message_length):
    x,y = np.shape(img)
    copy2 = img.copy()
    p_s = y // encoded_length * message_length
    parity = encoded_length - message_length
    for i in range(0,x):
        for j in range(0,int(y/encoded_length)):
            copy2[i][encoded_length*j:encoded_length*j+message_length] = img[i][message_length * j:message_length * j + message_length]
            copy2[i][encoded_length*j+message_length:encoded_length*j+encoded_length] = img[i][p_s + parity * j:p_s + parity * j + parity]
        if x % 30 == 0:
            await asyncio.sleep(0)
    return copy2

async def generate_noisy_image(input,numpy_array_to_copy):
    x,y = np.shape(numpy_array_to_copy)
    image_array = np.zeros((x,y))
    # % error amount
    scale = int(y*input/100)
    for i in range(0,x):
        for j in range(0,scale):
            integer = random.randrange(0,y,1)
            image_array[i][integer] = 1
        if x % 30 == 0:
            await asyncio.sleep(0)
    return image_array

def img_to_base64_str(img):
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    buffered.seek(0)
    img_byte = buffered.getvalue()
    img_str = "data:image/png;base64," + base64.b64encode(img_byte).decode()
    return img_str

def img_from_base64_str(msg):
    msg = msg.replace("data:image/png;base64,", "")
    msg = base64.b64decode(msg)
    buf = io.BytesIO(msg)
    img = Image.open(buf)
    return img

#Can store arrays like this, but also can store arrays like this.

# def store_image(numpy_binary_array,key):
#     list = numpy_binary_array.tolist()
#     js_array = json.dumps(list)
#     new_image = js.JSON.stringify(js_array)
#     window.sessionStorage.setItem(key,new_image)

# def display_stored_image(key, id):
#     image = window.sessionStorage.getItem(key)
#     js_array = js.JSON.parse(image)
#     list = json.loads(js_array)
#     numpy = np.array(list)
#     print(numpy)
#     image = binaryToImage(numpy) 
#     my_stream = io.BytesIO()
#     image.save(my_stream, format="PNG")
#     #Create a JS File object with our data and the proper mime type
#     image_file = File.new([Uint8Array.new(my_stream.getvalue())], "new_image_file.png", {type: "image/png"}) 
#     #Create new tag and insert into page
#     print(type(image_file))
#     new_image = document.createElement('img')
#     new_image.src = window.URL.createObjectURL(image_file)
#     document.getElementById(id).innerHTML = ""
#     document.getElementById(id).appendChild(new_image)



#Better storage method? This one does work
async def store_image(numpy_binary_array,key, sess='on'):
    console.log('enter stored image')
    img = await binaryToImage(numpy_binary_array)
    img_str = img_to_base64_str(img)
    js_string = json.dumps(img_str)
    if sess == 'on':
        window.sessionStorage.setItem(key,js_string)
    else:
        window.localStorage.setItem(key,js_string)

def display_stored_image(key,id, sess='on'):
    if sess == 'on':
        js_string = window.sessionStorage.getItem(key)
    else:
        js_string = window.localStorage.getItem(key)
    img_str = json.loads(js_string)
    img = img_from_base64_str(img_str)
    my_stream = io.BytesIO()
    img.save(my_stream, format="PNG")
    image_file = File.new([Uint8Array.new(my_stream.getvalue())], "new_image_file.png", {type: "image/png"}) 
    #Create new tag and insert into page
    new_image = document.createElement('img')
    new_image.src = window.URL.createObjectURL(image_file)
    document.getElementById(id).innerHTML = ""
    document.getElementById(id).appendChild(new_image)
    document.getElementById(id).className="animate"
    
def display_image(image,id):
    my_stream = io.BytesIO()
    image.save(my_stream, format="PNG")
    #Create a JS File object with our data and the proper mime type
    image_file = File.new([Uint8Array.new(my_stream.getvalue())], "new_image_file.png", {type: "image/png"})
    document.getElementById(id).innerHTML = ""
    #Create new tag and insert into page
    new_image = document.createElement('img')
    new_image.src = window.URL.createObjectURL(image_file)
    document.getElementById(id).appendChild(new_image)
    document.getElementById(id).className="animate"

async def hamming(e):
    #Get the first file from upload
    file_list = e.target.files
    first_item = file_list.item(0)
    #print(first_item)

    #Switch statements
    # await set_switch("switch1","on")
    #Get the data from the files arrayBuffer as an array of unsigned bytes
    array_buf = Uint8Array.new(await first_item.arrayBuffer())
    #print(array_buf)
    #BytesIO wants a bytes-like object, so convert to bytearray first
    bytes_list = bytearray(array_buf)
    #print(bytes_list)
    my_bytes = io.BytesIO(bytes_list) 
    #Create PIL image from np array
    my_image = Image.open(my_bytes)
    #1st is y, 2nd is x
    new_image = my_image.resize((400,300)) 
    rs_image = my_image.resize((200,150))
    #Log some of the image data for testing
    console.log(f"{my_image.format= } {my_image.width= } {my_image.height= }")
    #Refresh storage
    window.sessionStorage.clear()
    window.localStorage.clear()
    console.log("cleared storage")
    # Now that we have the image loaded with PIL, we can use all the tools it makes available. 
    # "Emboss" the image, rotate 45 degrees, fill with dark green
    #my_image = my_image.filter(ImageFilter.EMBOSS).rotate(45, expand=True, fillcolor=(0,100,50)).resize((300,300))
    new_image = await imageToBinary(new_image)
    await store_image(new_image,"og_blackandwhite")
    console.log('after store image')
    display_stored_image("og_blackandwhite","output_upload")
    console.log("step one")
    hamming_img = await img_encode(new_image,4)
    hamming_img = await seperate_img_hamming(hamming_img)
    await store_image(hamming_img,"ham")
    output_text(1,2)
    # display_stored_image("ham","output_upload_hamming")
    console.log('step two')
    #For 0.25%
    i = 1
    noise = await generate_noisy_image(i,hamming_img)
    await store_image(noise,"noise_"+str(i))
    noisy_image = convertFinite(hamming_img + noise,2)
    await store_image(noisy_image,"ham_n_"+str(i))
    output_text(2,1)
    for_correction = await rejoin_img_hamming(noisy_image)
    correction = await correct_img_hamming(for_correction)
    correction_sep = await seperate_img_hamming(correction)
    await store_image(correction_sep,"final_"+str(i))
    #the rest
    output_matrix(1,3)
    for i in range(2,10,2):
        noise = await generate_noisy_image(i,hamming_img)
        await store_image(noise,"noise_"+str(i))
        noisy_image = convertFinite(hamming_img + noise,2)
        await store_image(noisy_image,"ham_n_"+str(i))
        for_correction = await rejoin_img_hamming(noisy_image)
        correction = await correct_img_hamming(for_correction)
        correction_sep = await seperate_img_hamming(correction)
        await store_image(correction_sep,"final_"+str(i))
    console.log('first loop completed')
    rs_image = await imageToBinary(rs_image)
    for i in range(1,11,2):
        num = i
        parity = 4*num
        RSolo = await convertBintoRS(rs_image,8)
        RSolo = await encodeRS(RSolo, 5, parity)
        rs_img = await seperate_img(RSolo,5+parity,5)
        rs_img = await RStoBinary(rs_img,8)
        # binaryToImage(rs_img)
        await store_image(rs_img,"rs_"+str(i))
        #For 0.25%
        j = 0.5
        noise = await generate_noisy_image(2*j,rs_img)
        await store_image(noise,"noisy_"+str(i)+str(j),sess='off')
        #Add noise to image
        noisy_image = rs_img + noise
        #Apply finite field
        noisy_image = convertFinite(noisy_image,2)
        await store_image(noisy_image,"rs_noisy_"+str(i)+str(j),sess='off')
        #Do error correction
        ready4correct = await convertBintoRS(noisy_image,8)
        ready4correct = await rejoin_img(ready4correct,5+parity,5)
        correction = await correctRS_img(ready4correct,5+parity,parity)
        backagain = await seperate_img(correction,5+parity,5)
        correction_bin = await RStoBinary(backagain,8)
        await store_image(correction_bin,"rs_corr_"+str(i)+str(j),sess='off')
        #For the rest
        for j in range(1,5):
            noise = await generate_noisy_image(2*j,rs_img)
            await store_image(noise,"noisy_"+str(i)+str(j),sess='off')
            #Add noise to image
            noisy_image = rs_img + noise
            #Apply finite field
            noisy_image = convertFinite(noisy_image,2)
            await store_image(noisy_image,"rs_noisy_"+str(i)+str(j),sess='off')
            #Do error correction
            ready4correct = await convertBintoRS(noisy_image,8)
            ready4correct = await rejoin_img(ready4correct,5+parity,5)
            correction = await correctRS_img(ready4correct,5+parity,parity)
            backagain = await seperate_img(correction,5+parity,5)
            correction_bin = await RStoBinary(backagain,8)
            await store_image(correction_bin,"rs_corr_"+str(i)+str(j),sess='off')
    console.log('second and final loop')
            
    document.getElementById("loading_ani").classList.remove('lds-facebook') 
    error_c = document.getElementById("selection_box2").value
    noise_level = document.getElementById("selection_box3").value
    display_stored_image("rs_"+str(error_c),"reed_s")
    display_stored_image("noisy_"+str(error_c)+str(noise_level),"noisy_2",sess='off')
    display_stored_image("rs_noisy_"+str(error_c)+str(noise_level),"noisy_image_2",sess='off')
    display_stored_image("rs_corr_"+str(error_c)+str(noise_level),"corrected_2",sess='off')
    console.log('finished upload of rs')

# Run image processing code above whenever file is uploaded  
def backround_code(e):
    asyncio.ensure_future(hamming(e))

upload_file = create_proxy(backround_code)
document.getElementById("file-upload").addEventListener("change", upload_file)

#Code for image processing
def selectChange(event):
    choice = document.getElementById("selection_box1").value
    display_stored_image("noise_"+str(choice),"output_upload_noise")
    display_stored_image("ham_n_"+str(choice),"output_upload_noisy_image")
    display_stored_image("final_"+str(choice),"output_upload_corrected")
    if document.getElementById('row10_1').style.visibility == 'hidden':
        output_text(9,1)
        output_text(10,3)
        output_text(11,1)

def selectChange2(event):
    error_c = document.getElementById("selection_box2").value
    noise_level = document.getElementById("selection_box3").value
    display_stored_image("rs_"+str(error_c),"reed_s")
    display_stored_image("noisy_"+str(error_c)+str(noise_level),"noisy_2",sess='off')
    display_stored_image("rs_noisy_"+str(error_c)+str(noise_level),"noisy_image_2",sess='off')
    display_stored_image("rs_corr_"+str(error_c)+str(noise_level),"corrected_2",sess='off')
    if document.getElementById('row12_1').style.visibility == 'hidden':
        output_text(12,2)    

def selectChange3(event):
    error_c = document.getElementById("selection_box2").value
    noise_level = document.getElementById("selection_box3").value
    display_stored_image("rs_"+str(error_c),"reed_s")
    display_stored_image("noisy_"+str(error_c)+str(noise_level),"noisy_2",sess='off')
    display_stored_image("rs_noisy_"+str(error_c)+str(noise_level),"noisy_image_2",sess='off')
    display_stored_image("rs_corr_"+str(error_c)+str(noise_level),"corrected_2",sess='off')


# Create a JsProxy for the callback function
change_proxy = create_proxy(selectChange)
document.getElementById("selection_box1").addEventListener("change", change_proxy)
change_proxy2 = create_proxy(selectChange2)
document.getElementById("selection_box2").addEventListener("change", change_proxy2)
change_proxy3 = create_proxy(selectChange3)
document.getElementById("selection_box3").addEventListener("change", change_proxy3)

async def set_switch(key,text):
    await asyncio.sleep(0) 
    window.sessionStorage.setItem(key,json.dumps(text)) 
    
def change_switch(key):
    if json.loads(window.sessionStorage.getItem(key)) == "on":
        asyncio.ensure_future(set_switch(key,"off"))
        return 0
    else:
        return 1


#Function for interactive hamming
def selectChange_int_ham(event, G=G):
    if document.getElementById('output').style.visibility == 'hidden':
        output_text(3,1)
        output_text(4,1)
        document.getElementById('output').style.visibility='visible'
        document.getElementById('output2').style.visibility='visible'
        document.getElementById('equals1').style.visibility='visible'
        document.getElementById('equals2').style.visibility='visible'
        document.getElementById('output3').style.visibility='visible'
        document.getElementById('equals3').style.visibility='visible'
        document.getElementById('button1').style.visibility='visible'
    int1 = document.getElementById("int1").value
    int2 = document.getElementById("int2").value
    int3 = document.getElementById("int3").value
    int4 = document.getElementById("int4").value
    message_int = np.array([int1,int2,int3,int4],dtype='int32')
    message_int = message_int.transpose()
    encoded_int = np.matmul(G, message_int)
    finite = convertFinite(encoded_int, 2)
    copy_int = finite.copy()
    copy_int[4] = finite[0]
    copy_int[5] = finite[1]
    copy_int[0] = finite[2]
    copy_int[6] = finite[3]
    copy_int[1] = finite[4]
    copy_int[2] = finite[5]
    copy_int[3] = finite[6]
    incorrect = finite.copy()
    for i in range(0,7):
        flip = int(document.getElementById("flip"+str(i+1)).value)
        document.getElementById("out_c_"+str(i+1)).style.color=''
        if flip == 1:
            incorrect[i] = 1 - incorrect[i]
            document.getElementById("out_c_"+str(i+1)).style.color='red'
            if document.getElementById('matrix5_1').style.visibility == 'hidden':
                output_text(6,1)
                output_matrix(5,4)
                output_matrix(6,3)
                output_text(8,1)
                document.getElementById('decimal').style.visibility = 'visible'
    syndrome = np.matmul(H,incorrect)
    fin_syndrome = convertFinite(syndrome,2)
    fin_syndrome2 = np.zeros(3)
    for o in range(0,3):
        fin_syndrome2[o] = fin_syndrome[2-o]
    decimal = errorPlace(incorrect)
    correct = incorrect.copy()
    if decimal != 0:
        if correct[decimal - 1] == 0:
            correct[decimal - 1] = 1
        else:
            correct[decimal - 1] = 0
    final = [correct[2],correct[4],correct[5],correct[6]]
    #Write text
    for i in range(0,len(finite)):
        Element('out_b4_'+str(i+1)).write(str(encoded_int[i]))
        Element('out'+str(i+1)).write(str(finite[i]))
        Element('out_c_'+str(i+1)).write(str(incorrect[i]))
        Element('out_af_'+str(i+1)).write(str(copy_int[i]))
        Element('cor_'+str(i+1)).write(str(correct[i]))
    for i in range(0,len(syndrome)):
        Element('syn'+str(i+1)).write(str(syndrome[i]))
        Element('syn_b_'+str(i+1)).write(str(int(fin_syndrome2[i])))
    for i in range(0,4):
        Element('final'+str(i+1)).write(str(final[i]))
    Element('decimal').write(str(decimal))  


#Create proxies for interactive hamming
change_proxy_int1 = create_proxy(selectChange_int_ham)
document.getElementById("int1").addEventListener("change", change_proxy_int1)
document.getElementById("int2").addEventListener("change", change_proxy_int1)
document.getElementById("int3").addEventListener("change", change_proxy_int1)
document.getElementById("int4").addEventListener("change", change_proxy_int1)
document.getElementById("flip1").addEventListener("change", change_proxy_int1)
document.getElementById("flip2").addEventListener("change", change_proxy_int1)
document.getElementById("flip3").addEventListener("change", change_proxy_int1)
document.getElementById("flip4").addEventListener("change", change_proxy_int1)
document.getElementById("flip5").addEventListener("change", change_proxy_int1)
document.getElementById("flip6").addEventListener("change", change_proxy_int1)
document.getElementById("flip7").addEventListener("change", change_proxy_int1)


def button_callback1(event):
    display_stored_image("ham","output_upload_hamming")
    output_text(5,1)
    output_matrix(4,3)

document.getElementById("button1").addEventListener("click", create_proxy(button_callback1))

superscript_map = {
    "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶",
    "7": "⁷", "8": "⁸", "9": "⁹","10": "¹⁰","11": "¹¹","12": "¹²","13": "¹³","14": "¹⁴",
    "15": "¹⁵","16": "¹⁶","17": "¹⁷","18": "¹⁸","19": "¹⁹","20": "²⁰",
    "a": "ᵃ", "b": "ᵇ", "c": "ᶜ", "d": "ᵈ",
    "e": "ᵉ", "f": "ᶠ", "g": "ᵍ", "h": "ʰ", "i": "ᶦ", "j": "ʲ", "k": "ᵏ",
    "l": "ˡ", "m": "ᵐ", "n": "ⁿ", "o": "ᵒ", "p": "ᵖ", "q": "۹", "r": "ʳ",
    "s": "ˢ", "t": "ᵗ", "u": "ᵘ", "v": "ᵛ", "w": "ʷ", "x": "ˣ", "y": "ʸ",
    "z": "ᶻ", "A": "ᴬ", "B": "ᴮ", "C": "ᶜ", "D": "ᴰ", "E": "ᴱ", "F": "ᶠ",
    "G": "ᴳ", "H": "ᴴ", "I": "ᴵ", "J": "ᴶ", "K": "ᴷ", "L": "ᴸ", "M": "ᴹ",
    "N": "ᴺ", "O": "ᴼ", "P": "ᴾ", "Q": "Q", "R": "ᴿ", "S": "ˢ", "T": "ᵀ",
    "U": "ᵁ", "V": "ⱽ", "W": "ᵂ", "X": "ˣ", "Y": "ʸ", "Z": "ᶻ", "+": "⁺",
    "-": "⁻", "=": "⁼", "(": "⁽", ")": "⁾"}



def error_bytes(event, button_p = "no", map=superscript_map, array_but="id"):
    if document.getElementById("gen_pol1").style.visibility == "hidden":
        document.getElementById("gen_pol1").style.visibility = "visible"
        document.getElementById("gen_pol2").style.visibility = "visible"
        output_text(10,5)
        output_text(14,2)
    parity = document.getElementById("error_bytes").value
    console.log("inside error_bytes")
    Element("bytes_1").write(str(parity))
    mes_len = int(parity) + 5
    Element("bytes_2").write("("+str(mes_len)+","+str(5)+")")
    string = "(x &#43; 1) "
    for i in range(1, int(parity)):
        power = gf_pow(2, i)
        string += "&#8901; "
        string += "(x &#43; " + str(power) + ") "
    Element("gen_pol1").write(unescape(string))
    # init_tables()
    gen = rs_generator_poly(int(parity))
    string2 = "G(x) =   x" + map[str(len(gen)-1)] + " + "
    for i in range(1,len(gen)-1):
        string2 += str(gen[i])
        if gen[i] == 0:
            string2 += ""
        if len(gen)-1-i == 1:
            string2 += "x" + " + "
        else:
            string2 += "x" + map[str(len(gen)-1-i)] + " + "
    string2 += str(gen[-1])
    Element("gen_pol2").write(string2)
    console.log(str(Element("rs_mes")))
    if button_p == "yes":
        int_array = []
        for i in range(0,5):
            int_array.append(random.randrange(0,255,1))
        Element("rs_mes").write(str(int_array))
        document.getElementById("switch1").style.color = "red"
        window.sessionStorage.setItem("string3",json.dumps(str(int_array)))
    string_list = json.loads(window.sessionStorage.getItem("string3"))
    list_ = string_list.strip("][").split(", ")
    int_array1 = [int(i) for i in list_]
    int_array = int_array1 + [0] * (len(gen)-1)
    string3 = "M(x) =   "
    for i in range(0,5):
        string3 += str(int_array[i])
        # console.log(string3)
        if len(int_array)-1-i == 1:
            string3 += "x" + " + "
            # console.log(string3)
        else:
            string3 += "x" + map[str(len(int_array)-1-i)] + " + "
            # console.log(string3)
    string3 = string3[:-3]
    Element("rs_mes2").write(string3)
    _,remainder = gf_poly_div(int_array,gen)
    string4 = "R(x) =   "
    for i in range(0,len(remainder)):
        string4 += str(remainder[i])
        # console.log(string4)
        if len(remainder)-1-i == 0:
            string4 += " + "
        elif len(remainder)-1-i == 1:
            string4 += "x" + " + "
            # console.log(string4)
        else:
            string4 += "x" + map[str(len(remainder)-1-i)] + " + "
            # console.log(string4)
    string4 = string4[:-3]
    Element("remainder").write(string4)
    enc_msg = int_array1+remainder
    # console.log(document.getElementById("switch1").style.color)
    new_msg = enc_msg
    col_msg = [0]*len(enc_msg)
    Element("enc_mes").write(str(enc_msg))
    for i in range(0,len(enc_msg)):
        if "enc_msg_"+str(i) == array_but:
            if document.getElementById("row18_1").style.visibility == "hidden":
                output_text(18,4)
                output_text(11,1)
                output_text(17,1)
                document.getElementById("fourney_syn").style.visibility = "visible"
                document.getElementById("BM_loc").style.visibility = "visible"
                document.getElementById("err_pos").style.visibility = "visible"
                document.getElementById("final_mes").style.visibility = "visible"
            if document.getElementById("switch1").style.color == "red":
                document.getElementById("switch1").style.color = ""
                new_msg = enc_msg
                col_msg = [0]*len(enc_msg)
            else:
                string_list_ = json.loads(window.sessionStorage.getItem("string4"))
                _list_ = string_list_.strip("][").split(", ")
                new_msg = [int(i) for i in _list_]
                string_list__ = json.loads(window.sessionStorage.getItem("string5"))
                _list__ = string_list__.strip('][').split(", ")
                col_msg = [int(i) for i in _list__]
            if col_msg[i] == 0:
                new_msg[i] = random.randrange(0,255,1)
                col_msg[i] = 1
            else:
                new_msg[i] = enc_msg[i]
                col_msg[i] = 0     
            window.sessionStorage.setItem("string4",json.dumps(str(new_msg)))
            window.sessionStorage.setItem("string5",json.dumps(str(col_msg)))

    text = document.getElementById('enc_mes2')
    text.innerHTML = ""
    text.appendChild(document.createTextNode("["))
    for i in range(0,len(new_msg)):      
        element = document.createElement("button")
        element.setAttribute("id","enc_msg_"+str(i))
        element.setAttribute("type","button")
        element.innerHTML = str(new_msg[i])
        if col_msg[i] == 0:
            element.style.color = "black" 
        else:
            element.style.color = "red" 
        text.appendChild(element)
        if i == len(new_msg)-1:  
            text.appendChild(document.createTextNode("]"))
        else:
            text.appendChild(document.createTextNode(", "))
        #Create proxies for each button
        function(i)   
    syndrome = rs_calc_syndromes(new_msg, int(parity))
    # Element("fourier").write(str(syndrome))
    fourney_syn = rs_forney_syndromes(syndrome,[],len(new_msg))
    Element("fourney_syn").write(str(fourney_syn))
    # compute the error locator polynomial using Berlekamp-Massey
    err_loc = rs_find_error_locator(fourney_syn, int(parity), erase_count=0)
    Element("BM_loc").write(str(err_loc))
    # locate the message errors using Chien search (or brute-force search)
    err_pos = rs_find_errors(err_loc[::-1], len(new_msg))
    Element("err_pos").write(str(err_pos))
    # if err_pos is None:
    # raise ReedSolomonError("Could not locate error")  # error location failed
    # Find errors values and apply them to correct the message
    # compute errata evaluator and errata magnitude polynomials, then correct errors and erasures
    msg_out = rs_correct_errata(new_msg, syndrome, (err_pos))  # note that we here use the original syndrome, not the forney syndrome
    Element("final_mes").write(str(msg_out))
    # (because we will correct both errors and erasures, so we need the full syndrome)

#Create proxies for each button
def function(z):      
    ol_string = "enc_msg_"+str(z)
    btn = document.getElementById(ol_string)
    wrappers.add_event_listener(btn,"click",lambda event: error_bytes(event,array_but=ol_string))

def init_change(event):
    document.getElementById("switch1").style.color = "red"
    error_bytes(event)

def gen_mes(event):
    console.log('button2 pressed')
    if document.getElementById("rs_mes").style.visibility == "hidden":
        document.getElementById("rs_mes").style.visibility = "visible"
        document.getElementById("rs_mes2").style.visibility = "visible"
        document.getElementById("remainder").style.visibility = "visible"
        document.getElementById("enc_mes").style.visibility = "visible"
        output_text(15,3)
        document.getElementById("button3").style.visibility = "visible"
    error_bytes(event,button_p="yes")

def display_rs(event):
        if document.getElementById("row16_1").style.visibility == "hidden":
            display_stored_image("rs_1","demo_rs_enc")
            output_text(16,1)
            document.getElementById("enc_mes2").style.visibility = "visible"

document.getElementById("error_bytes").addEventListener("change", create_proxy(init_change))
document.getElementById("button2").addEventListener("click", create_proxy(gen_mes))
document.getElementById("button3").addEventListener("click", create_proxy(display_rs))

def output_text(row,num):
    for i in range(0,num):
        document.getElementById('row'+str(row)+'_'+str(i+1)).style.visibility='visible'
        document.getElementById('row'+str(row)+'_'+str(i+1)).className='animate glow'

def output_matrix(row,num):
    for i in range(0,num):  
        document.getElementById('matrix'+str(row)+'_'+str(i+1)).style.visibility='visible'

# async def main()7
#     while True7

# async def main():
#     while True:
#         loading()
#         callback()
#         hamming()
#         await asyncio.sleep(0)
# asyncio.create_task(main())
# pyscript.create_task(main())
console.log("default script completed")




# create a new plot with default tools, using figure


# global bits_g
# bits_g = 8
# p = Slider(start=0.1, end=10, value=1, step=.1, title="Amplitude")
# div = Div(text=f'Amplitude is: {p.value}')

# def callback(attr, old, new):
#     div.text = f'Symbol is: {new}'
#     first_item = localStorage.getItem('key')
#     print(first_item)
#     my_image = imageToBinary(first_item)
#     print(my_image)
#     rs_img = convertBintoRS(my_image,8)
#     rs_img = encodeRS(rs_img, 5, 6)
#     rs_img = seperate_img(rs_img,5+6,5)
#     rs_img = RStoBinary(rs_img,8)
#     rs_img = binaryToImage(rs_img)
#     display_image(rs_img,"reed_s")

# p.on_change('value', callback)

# row = Row(children=[p, div])


# def doc_json(model, target):
#     with OutputDocumentFor([model]) as doc:
#         doc.title = ""
#         docs_json, _ = standalone_docs_json_and_render_items(
#             [model], suppress_callback_warning=False
#         )

#     doc_json = list(docs_json.values())[0]
#     root_id = doc_json['roots']['root_ids'][0]

#     return doc, json.dumps(dict(
#         target_id = target,
#         root_id   = root_id,
#         doc       = doc_json,
#         version   = __version__,
#     ))

# def _link_docs(pydoc, jsdoc):
#     def jssync(event):
#         if getattr(event, 'setter_id', None) is not None:
#             return
#         events = [event]
#         json_patch = jsdoc.create_json_patch_string(pyodide.ffi.to_js(events))
#         pydoc.apply_json_patch(json.loads(json_patch))

#     jsdoc.on_change(pyodide.ffi.create_proxy(jssync), pyodide.ffi.to_js(False))

#     def pysync(event):
#         json_patch, buffers = process_document_events([event], use_buffers=True)
#         buffer_map = {}
#         for (ref, buffer) in buffers:
#             buffer_map[ref['id']] = buffer
#         jsdoc.apply_json_patch(JSON.parse(json_patch), pyodide.ffi.to_js(buffer_map), setter_id='js')

#     pydoc.on_change(pysync)

# async def show(plot, target):
#     pydoc, model_json = doc_json(plot, target)
#     views = await Bokeh.embed.embed_item(JSON.parse(model_json))
#     jsdoc = views[0].model.document
#     _link_docs(pydoc, jsdoc)

# asyncio.ensure_future(show(row, 'myplot'))

