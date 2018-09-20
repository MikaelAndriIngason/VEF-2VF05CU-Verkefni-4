<h1>Verkefni 4.1 - JSON</h1><hr>

% for x in range(0,len(gogn['results'])):
     <p>{{gogn['results'][x]["shortName"]}} | {{gogn['results'][x]["longName"]}} | {{gogn['results'][x]["value"]}} | {{gogn['results'][x]["askValue"]}} | {{gogn['results'][x]["bidValue"]}} | {{gogn['results'][x]["changeCur"]}} | {{gogn['results'][x]["changePer"]}}</p>
% end

<hr><br><a href="/">< Til baka</a>
