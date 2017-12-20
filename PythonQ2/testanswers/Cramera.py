# -*- coding: utf-8 -*-
"""
Cramer.py -- Regel van Cramer gebruiken om Ax=b op te lossen.

    Opdrachtbeschrijving
    --------------------
    In je reader, Blok 2 is een toepassingsprobleem gegeven, waarin twee
    lijnen L1 en L2:
        
        L1:  4x + 2y = -2
        L2: -3x +  y =  1
        
    elkaar snijden in het punt s = (-2/5, -1/5). We gaan in deze 
    opdracht het resultaat van deze berekening controleren door gebruik
    te maken van de Regel van Cramer.
    
    We schrijven: A.X = b, ofwel:
        
             (  4   2 )   (x)    (-2)
        A =  (        ) . ( )  = (  )
             ( -3   1 )   (y)    ( 1)
        
    Je herkent direct A en vector b. Kolomvector X is het snijpunt 
    van L1 en L2. We kunnen dit snijpunt X=(x,y)^t uitrekenen, als volgt:
        
        (x)        ( |-2  2| )
        ( )    1   ( | 1  1| )
    X=  ( ) = ---  (         )   (1): Toepassing van de Regel van Cramer
        (y)   |A|  ( | 4 -2| )
        ( )        ( |-3  1| )
        
    Je ziet in (1) dat we x en y vinden door twee keer een determinant uit
    te rekenen, en die dan te vermenigvuldigen met 1/|A| . Determinant |A|
    is duidelijk, maar wat zijn de twee determinanten in de meest rechtse 
    kolomvector in (1)? Je vindt deze determinanten door achtereenvolgens 
    de eerste en de tweede kolom vector in A vervangen door vector b, die 
    is gegeven, en van die matrix die je dan krijgt, de determinant uit te
    rekenen. In formule:
        
              det(A_i)
        x_i = -------,      (2): de Regel van Cramer
               det(A)
               
    In (2), de Regel van Cramer, staat x_i resp. dus voor x en voor y, en 
    A_i voor matrix A met kolomvector i vervangen door vector b=(-2,1)^t .
    
    OPDRACHT
    --------
    Zie OPDRACHTEN blad Oefentoets
    
    TEMPLATE
    --------
    Gebruik deze template voor je programma en introduceer
    zelf GEEN NIEUWE VARIABELEN. Houd je aan de bestaande
    namen voor variabelen, functies e.d. Wijzig die niet.
    
@author: Bart Gerritsen
"""

def det2(A):
    """
    Bereken 2x2 determinant
    
    input : A, 2x2 matrix(list-of-lists of floats), matrix waarvan determinant
               moet worden berekend
    return: |A| (float waarde van de determinant)
    """
    assert len(A)==2 and len(A[0])==2,'det2 function is only for 2 by 2'
    return A[0][0]*A[1][1] - A[0][1]*A[1][0]

def solve(A,b):
    """
    bepaal X in system AX=b, door toepassing van de Regel van Cramer
    
    input : A, NxM matrix(list-of-lists of floats), systeemmatrix in A.X=b
    return: X, vector van floats, de gevonden oplossingsvector met Cramer
    """
    # bepaal de dimensies van het systeem  ...
    N,M = len(A), len(A[0])
    assert any(A), 'cannot solve this system'
    assert N==M, 'system matrix must be square'
    
    # full determinant ...
    D = det2(A)
    # maak een lege vector die we gaan vullen met x_i elementen ...
    X = []
    
    for i in range(N):
        Ai = []                         # lege lijst die N rows gaat bevatten
        for r in range(N):
            Ai.append([])               # lijst die M elementen gaat bevatten
            for c in range(M):
                if c == i:
                    Ai[r].append(b[r])  # vervang deze door elem b
                else:
                    Ai[r].append(A[r][c])
        X.append( det2(Ai)/D )          # pas regel van Cramer toe en voeg
                                        # zo gevonden x_i toe aan vector X
    return X

def main():
    # system matrix A in:  Ax=b
    A = [ [  4, 2 ],
          [ -3, 1 ]]
    # gegeven vector b ...
    b = [ -2, 1 ]
    # max verschil toegestaan (voor eindtest resultaat)
    DELTA = 1.0e-06
    
       
    # bepaal oplossing X met solve() op basis van Reggel van Cramer   
    X = solve(A,b)
    
    print('Mijn oplossing met Cramer: X={:s}'. format(str(X)))
    
    B = [ float('NaN'), float('NaN') ]
    D = [ float('NaN'), float('NaN') ]
    
    inaccurate = False
    for n in range(len(b)):
        B[n] = A[n][0]*X[0]+A[n][1]*X[1]
        # het verschil met de gegeven b
        D[n] = B[n] - b[n]
        if not abs(D[n]) < DELTA:
            inaccurate = True
            
    # check het resultaat: toch niet inaccuraat??
    if inaccurate:
        result = 'NOT OK'
    else:
        result = 'OK'
    
    # druk jouw verschilvector D af ...
    print('Mijn verschilvector D = B-b = AX-b: {:s} ... {:s}'. \
          format(str(D),result))
    
main()