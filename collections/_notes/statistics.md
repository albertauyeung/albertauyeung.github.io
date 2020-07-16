---
layout: article
title:  "Statistics"
tags: [statistics]
---

<h1>Basic Notions</h1>
<ul>
<li><b>Sample Standard Deviation</b> is defined as:
<blockquote>
$\displaystyle{
s = \sqrt{variance} = \sqrt{\frac{\sum_{i=1}^n{(x_i -  \overline{x})^2}}{n-1}}
}$
</blockquote>
Note: (n-1) is the <b>degree of freedom</b> associated with the variance. Since the devations add to 0, a specification of any n-1 deviations allos us to recover the one that is left out. The divisor (n-1) represents the number of deviations that can be viewed as free quantities.
<li>The importance of graphics: see Tufte (1983)
<li><b>Parameter</b>: A parameter is a numerical feature of a population. Examples are the population mean and the population variance. A parameter is usually an unknown quantity, which can only be correctly determined by a complete study of the population.
<li><b>Statistic</b>: A statistic is a numerical valued function of the sample observations. Examples are the sample mean and the sample variance.
<li>A statistic serves as a source of information about the value of a parameter.
<li><b>Sampling distribution</b>: the probability distribution of a statistic. (For example: we may talk about the sampling distribution of the sample mean)
<li>When doing sampling, a unit needs to be replaced after each selection so that the probability distribution of the population is the same every time. However, for very large population size and relatively small sample size, it is inconsequential whether or not a unit is replaced.
<li><b>Mean and Standard Deviation of $\overline{X}$</b>:
<blockquote>$\displaystyle{ E(\overline{X}) = \mu \quad\quad \textrm{(= population mean})}$</blockquote>
<blockquote>$\displaystyle{ Var(\overline{X}) = \frac{\sigma^2}{n} }$</blockquote>
<blockquote>$\displaystyle{ sd(\overline{X}) = \frac{\sigma}{\sqrt{n}} }$</blockquote>
<li><b>Central Limit Theorem</b>: Whatever the population, when $n$ is large the distribution of $\overline{X}$ is approximately normal with mean $\mu$ and standard deviation $\sigma / \sqrt{n}$.
<blockquote>$\displaystyle{
Z = \frac{\overline{X} - \mu}{\sigma / \sqrt{n}} \quad\quad \textrm{is approximately N(0,1)}
}$</blockquote>
</ul>

<br>

<h1>Statistical Inference</h1>
<ul>
<li>Two important types of inferences: (1) <b>estimation of parameters</b> and (2) <b>testing of statistical hypotheses</b>.
<li><b>Confidence Interval</b>
<ul>
<li><b>Level of confidence</b>: the probability that before sampling the proposed interval will contain the true value of the parameter being estimated. Typical values are 0.90, 0.95, and 0.99.
<li>Assuming that the population standard deviation is known, for $\overline{X}$ we have:
<blockquote>$\displaystyle{
P( \mu - 1.96\frac{\sigma}{\sqrt{n}} < \overline{X} < \mu + 1.96\frac{\sigma}{\sqrt{n}}) = 0.95
}$</blockquote>
That is, the probability that $\mu$ lies in the interval is 0.95
<li>The above probability statement can be rewritten as:
<blockquote>$\displaystyle{
P( \overline{X} - 1.96\frac{\sigma}{\sqrt{n}} < \mu < \overline{X} + 1.96\frac{\sigma}{\sqrt{n}}) = 0.95
}$</blockquote>
Since $\sigma$ is known, both the upper and lower endpoints can be computed as soon as the sample data are available.
<li>We sa that $(\overline{x} - 1.96\sigma/\sqrt{n}, \overline{x} + 1.96\sigma/\sqrt{n})$ is a 95% confidence interval for $\mu$.
<li>The probability, e.g. 0.95, is interpreted as the long-run relative frequency over many repetitions of sampling asserts that about 95% of the intervals will cover $\mu$.
<li>In many situations, however, $\sigma$ is unknow. When $n$ is large, we can replace $\sigma/\sqrt{n}$ with its estimator $S\sqrt{n}$ without affecting the probability statement. Hence, a $100(1-\alpha)%$ confidence interval for $\mu$ is given by:
<blockquote>$\displaystyle{
(\overline{X} - z_{\alpha/2}\frac{S}{\sqrt{n}} \quad , \quad \overline{X} + z_{\alpha/2}\frac{S}{\sqrt{n}})
}$</blockquote>
where $S$ is the sample standard deviation.
</ul>

<li><b>Hypotheses Testing</b>
<ul>
<li>$H_0$: the null hypothesis
<li>$H_1$: the alternative hypothesis, the claim or the research hypothesis that we wish to establish
<li>Hypotheses testing is to ask the question `Is there strong evidence for rejecting $H_0$?' This is similar to a coutr trial in which the jury clings to the null hypothesis of 'not guilty' unless there is convincing evidence that the suspect is guilty.
<li>Test criterion: a decision rule should be of the form (an example)
<blockquote>$\displaystyle{
\textrm{Reject} \;\; H_0 \;\; \textrm{if} \;\; \overline{X} \leq c
}$</blockquote>
<blockquote>$\displaystyle{
\textrm{Retain} \;\; H_0 \;\; \textrm{if} \;\; \overline{X} > c
}$</blockquote>
where $c$ is called the <b>critical value</b>
<li><b>Type I Error</b>: Rejecting $H_0$ when it is true. The probability of making a Type I error is $\alpha$.
<li><b>Type II Error</b>: Not rejecting $H_0$ when $H_1$ is true. The probability of making a Type II error is $\beta$.
<li>With a large sample size, a test based $Z$ is called a <b>large-sample normal test</b> or a <b>Z-test</b>.
<li><b>P-value</b> or <b>significant probability</b>: The probability, calculated under $H_0$, that the test statistic takes a value equal to or more extreme that the value actually observed. It serves as a measure of the strength of evidence against $H_0$. In other words, it is the smallest $\alpha$ that would permit rejection of $H_0$.
</ul>

<li><b>Small-sample Inferences for Normal Populations</b>
<ul>
<li>When the sample size is small (say less than 30), estimating $\sigma$ with $S$ does make a substantial difference. The standard normal variable $Z$ is no longer applicable as the the standard deviation can be larger than 1 due to the variability introduced by replacing $\sigma$ with $S$.
<li>Instead, <b>Student's $t$ distribution</b> (with $n-1$ degrees of freedom) is used:
<blockquote>$\displaystyle{
T = \frac{\overline{X}-\mu}{S/\sqrt{n}}
}$</blockquote>
<li>The qualification of 'with $n-1$ degrees of freedom' is important, because for each different sample size (value of $n-1$) there is a different $t$ distribution.
<li>With increasing degrees of freedom, the $t$ distribution approaches a normal distribution.
<li>A $100(1-\alpha)%$ confidence interval for a normal population mean:
<blockquote>$\displaystyle{
(\overline{X} - t_{\alpha/2}\frac{S}{\sqrt{n}} \quad , \quad \overline{X} + t_{\alpha/2}\frac{S}{\sqrt{n}})
}$</blockquote>
where $t_{\alpha/2}$ is the upper $\alpha/2$ point of the $t$ distribution with $d.f. = n-1$.
<li><b>Student's $t$-test</b>: a hypotheses test for $\mu$ with small samples.
</ul>

<li><b>Inferences about the Standard Deviation $\sigma$</b>
<ul>
<li>Sometimes the population variability may also be of interest. For example, in quality control, an engineer must ensure that the variability of the measurements does not exceed a specified limit.
<li>The sample standard deviation $S$ can be used as the point estimator of $\sigma$.
<li>The sampling distribution of $S^2$ is related to the $\chi^2$ distribution, whose form depends on $n-1$ (the degrees of freedom). Let $X_1,...,X_n$ be a random sample from a normal population $N(\mu,\sigma)$:
<blockquote>$\displaystyle{
\chi^2 = \frac{\sum_{i=1}^n{(X_i - \overline{X})^2}}{\sigma^2} = \frac{(n-1)S^2}{\sigma^2}
}$</blockquote>
<li>A $95%$ confidence interval for $\sigma$:
<blockquote>$\displaystyle{
( \quad S\sqrt{\frac{n-1}{\chi_{.025}^2}} \quad , \quad S\sqrt{\frac{n-1}{\chi_{.975}^2}} \quad )
}$</blockquote>
</ul>

<li><b>Comparing two treatments</b>
<ul>
<li><b>Treatment</b>: the things that are being compared
<li><b>Experimental units or subjects</b>: the basic units (e.g. person) that are exposed to one treatment or another
<li><b>Response</b>: the characteristic that is recorded after the application of a treatment to a subject
<li><b>Experimental design</b>: the manner in which subjects are chosen and assigned to treatments. Two basic types of design are (1) independent samples and (2) matched pair sample
<li>Independent samples refer to a case in which the subjects are randomly divided into two groups.
<li>Matched pair sample design refers to a case in which experimental subjects are chosen in pairs so that the members in each pair are alike, whereas those in different pairs may be substantially dissimilar.
</ul>

</ul>

<br>

<h1>Correlation Coefficient</h1>
<ul>
<li><b>Contingency tables</b>: A two-way frequency table which is used to summarise bivariate data.
<li>The correlation coefficient, denoted by $r$, is a measure of strength  of the linear relation between the $x$ and $y$ variables.
<blockquote>
$\displaystyle{
r = \frac{1}{n-1}\sum_{i=1}^n{(\frac{x_i - \overline{x}}{s_x})(\frac{y_i - \overline{y}}{x_y})}
}$
</blockquote>
<li><b>Spurious</b>: an observed correlation between two variables may be spurious, meaning that it may be caused by the influence of a third variable.
</ul>

<br>

<h1>References</h1>
<ul>
<li>Johnson, R. A, Bhattacharyya, G. L. (2001) Statistics - Principles and Methods. New York: John Wiley &amp; Sons, Inc.
<li>Tufte, T. R. (1983) The Visual Display of Quantitative Information. Cheshire, CT: Graphics Press.
</ul>
