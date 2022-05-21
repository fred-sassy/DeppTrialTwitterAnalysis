# DeppTrialTwitterAnalysis

I watched the testimony in the Johnny Depp v. Amber Heard trial where the guy from Berkeley Research Group explained his methodology, showed his final graphs, and said they were paid $600/hr to do it. I was pretty sure that amount of work could be done in an afternoon, so I gave it a go and it took way less time that even I thought. <br>

Final graphs are located in [this google sheet](https://docs.google.com/spreadsheets/d/1K7RzDF6lfR-5NwtZ3l-YI-FcFfocCSaPXaJXUvsR6TU/edit?usp=sharing).

### Methodology
I wasn't going to pay to use twitter's full archive, so I just used the last 7 days as that's free. In fairness, this expense would have played a role in the high price tag. To mimic the amount of analytical work actually done, I used an hourly breakdown of the last 7 days instead of the daily breakdown presented in court. <br>
I got this data from twitter's search api (`https://api.twitter.com/2/tweets/counts/recent`), counting the uses of the following hashtags:
 - #JusticeforJohnnyDepp
 - #AmberHeardIsAnAbuser
 - #AmberHeardIsALiar
 - #JohnnyDeppIsInnocent
 - #AmberTurd (peek what happens to this one after he testifies and the public learns it exists)
<br>
<br>
If you or anyone you know needs simple analytics work done, I will beat the Berkeley Research Group's rate at a fair $598/hr.
