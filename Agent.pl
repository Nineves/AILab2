%Agent.pl

%– implements Agent’s reset due to arriving into a cell inhabited by the Wumpus
reborn:-
assertz(hasarrow),
retractall(visited(_,_)),
assertz(visited(0,0)),
retractall(wumpus(_,_)),
retractall(confundus(_,_)),
retractall(tingle(_,_)),
retractall(glitter(_,_)),
retractall(stench(_,_)),
retractall(safe(_,_)),
retractall(current(_,_,_)),
assertz(current(0,0,rnorth))


%– implement Agent’s reasoning response to executing action A and receiving sensory input L.

:- dynamic hasarrow/0.
:- dynamic wumpusalive/0.
:- dynamic coins/0.
:- dynamic visited/2.
:- dynamic current/3.
:- dynamic tingle/2.
:- dynamic glitter/2.
:- dynamic stench/2.
:- dynamic safe/2.
:- dynamic tingle/2.

action(V) :- 
member(V,[shoot,moveforward,turnleft,turnright,pickup])



%L = [Confounded, Stench, Tingle, Glitter, Bump, Scream]
move(A,L) :-  
(A == shoot, hasarrow, nth0(5,L,on)); 			% the wumpus is dead and the agent loses arrow.
(A == shoot, hasarrow, nth0(5,L,off) -> retractall(hasarrow)); 			% the agent loses arrow
(A == moveforward, nth0(0,L,on), reposition());
(A == moveforward, nth0(4,L,off), current(X,Y,D), forward(X,Y,D), current(A,B,C), nth0(1,L,on)->assertz(stench(A,B));
         nth0(2,L,on)->assertz(tingle(A,B)); 
         nth0(3,L,on)->assertz(glitter(A,B)));
(A == moveforward, nth0(4,L,on));
(A == turnleft, current(X,Y,D),turnLeft(D,N),retractall(current(_,_,_)),assertz(current(X,Y,N)));
(A == turnright, current(X,Y,D),turnRight(D,N),retractall(current(_,_,_)),assertz(current(X,Y,N)));
(A == pickup, current(X,Y,D), nth0(3,L,on) -> reatractall(glitter(X,Y)));


move(A,L) :-
updateKB(L),(
(current(X,Y,D),nth0(3,L,on) -> (A is pickup, retractall(glitter(X,Y))); %if glitter then pick up the coin
(current(X,Y,D), hasarrow, inSameDirection(X,Y,D) -> (A is shoot, retractall(hasarrow)) );
(current(X,Y,D), nth0(4,L,off), D == rnorth, safe(X,Y-1)) -> (A is moveforward));
(current(X,Y,D), nth0(4,L,off), D == rsouth, safe(X,Y+1)) -> (A is moveforward));
(current(X,Y,D), nth0(4,L,off), D == rwest, safe(X-1,Y)) -> (A is moveforward));
(current(X,Y,D), nth0(4,L,off), D == reast, safe(X+1, Y)) -> (A is moveforward));
(current(X,Y,D), nth0(4,L,on)) - > (A is turnright)); %Bump at wall
？？？ How will the agent decide how to move(path finding?)


).

adjacent(X1,Y1,X2,Y2) :-
(X1 == X2, Y1 == Y2-1;Y1 == Y2+1);
(Y1 == Y2, X1 == X2-1;X1 == X2+1).

updateKB(L) :-
(nth0(1,L,on), current(X,Y,D), adjacent(X,Y,X2,Y2))->stench(X2,Y2));
(nth0(2,L,on), current(X,Y,D), adjacent(X,Y,X2,Y2))->tingle(X2,Y2));
(nth0(5,L,on)-> retractall(wumpusalive));
(nth0(3,L,on), current(X,Y,D), glitter(X,Y));
(nth0(0,L,on), current(X,Y,D), confundus(X,Y));



forward(X,Y,D) :-

current(X,Y,D),
(D == rnorth -> retractall(current(_,_,_)), assertz(current(X,Y+1,D)), assertz(visited(X,Y+1)));
(D == rwest -> retractall(current(_,_,_)), assertz(current(X-1,Y,D)), assertz(visited(X-1,Y)));
(D == reast -> retractall(current(_,_,_)), assertz(current(X+1,Y,D)), assertz(visited(X+1,Y)));
(D == rsouth -> retractall(current(_,_,_)), assertz(current(X,Y-1,D)), assertz(visited(X,Y-1))).

%if the agent is in the same direction with the agent
inSameDirection(X,Y,D):-

(D == rnorth, Wumpus(X,K), K > Y);
(D == rsouth, Wumpus(X,K), K < Y);
(D == rwest, Wumpus(S,Y), S < X);
(D == reast, Wumpus(S,Y), S > X);


reposition(L):-
safe(X1,Y1),
nth(0,L,on),
stench(X1,Y1)-> nth(1,L,on),
tingle(X1,Y1)-> nth(2,L,on),
glitter(X1,Y1) -> nth(3,L,on), 
retractall(visited(_,_)),
assertz(visited(0,0)),
retractall(current(_,_,_)),
asserts(current(0,0,rnorth)).


%initialize the agent
current(0,0,rnorth).
visited(0,0).
safe(0,0).


safe(X,Y) :-
\+ wumpus(X,Y), \+confundus(X,Y).

wumpus(X,Y) :- 
\+ (adjacent(X,Y,X2,Y2),visited(X2,Y2), \+stench(X2,Y2)).

confundus(X,Y) :-
\+ (adjacent(X,Y,X2,Y2),tingle(X2,Y2), \+tingle(X2,Y2)).



explore(L) :-

%not sure about this part, I think it needs recursion.



%change of direction
turnLeft(rnorth,rwest).
turnLeft(rwest,rsouth).
turnLeft(rsouth,reast).
turnLeft(reast,rnorth).
turnRight(rnorth,reast).
turnRight(rwest,rnorth).
turnRight(rsouth,rwest).
turnRight(reast,rsouth).

