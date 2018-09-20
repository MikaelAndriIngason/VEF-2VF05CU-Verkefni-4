<h1>Verkefni 4.2 - API</h1><hr>

<table>
    <tr>
        <th>Long name</th>
        <th>Short name</th>
        <th>Value</th>
    </tr>
    % for x in range(0,len(data['results'])):
        <tr>
            <td>{{data['results'][x]["longName"]}}</td>
            <td>{{data['results'][x]["shortName"]}}</td>
            <td>{{data['results'][x]["value"]}}</td>
        </tr>
    % end
</table>

<hr><br><a href="/">< Til baka</a>
